#!/usr/bin/env python3
"""Recompute and check committed data; default execution never rewrites it."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy

from phase_noise import (
    EIGENVALUE_CUTOFF,
    INFINITE_PRODUCT_SPINS,
    PSD_TOLERANCE,
    RATE_ABSOLUTE_TOLERANCE,
    TRACE_TOLERANCE,
    check_exact_endpoints,
    compute_suite,
)


DIRECTORY = Path(__file__).resolve().parent
JSON_REFERENCE = DIRECTORY / "reference-data.json"
CSV_REFERENCE = DIRECTORY / "reference-data.csv"
RATE_FIELDS = (
    "environment_entropy_bits",
    "flat_input_coherent_information_bits",
    "coherent_information_over_log2_d",
)
BOUND_FIELD = "infinite_product_entropy_error_bound_bits"


def row_key(row):
    return (row["d"], row["bath_spins"], row["gaussian_sigma_radians"])


def load_reference():
    payload = json.loads(JSON_REFERENCE.read_text())
    rows = payload["rows"]
    csv_rows = []
    with CSV_REFERENCE.open(newline="") as handle:
        for row in csv.DictReader(handle):
            parsed = {key: float(value) for key, value in row.items() if key != "bath_spins"}
            parsed["d"] = int(row["d"])
            parsed["bath_spins"] = (
                "infinite" if row["bath_spins"] == "infinite" else int(row["bath_spins"])
            )
            csv_rows.append(parsed)
    if rows != csv_rows:
        raise AssertionError("Committed JSON and CSV reference rows disagree.")
    return rows


def compare_reference(actual, expected):
    actual_by_key = {row_key(row): row for row in actual}
    expected_by_key = {row_key(row): row for row in expected}
    if len(actual_by_key) != len(actual) or len(expected_by_key) != len(expected):
        raise AssertionError("Duplicate parameter rows.")
    if actual_by_key.keys() != expected_by_key.keys():
        raise AssertionError("The recomputed suite and reference parameter sets differ.")
    largest_difference = 0.0
    for key, row in actual_by_key.items():
        reference = expected_by_key[key]
        if row["mean_photons"] != reference["mean_photons"]:
            raise AssertionError(f"Mean-photon convention differs at {key}.")
        for field in RATE_FIELDS:
            difference = abs(row[field] - reference[field])
            largest_difference = max(largest_difference, difference)
            if difference > RATE_ABSOLUTE_TOLERANCE:
                raise AssertionError(f"Reference mismatch: {key}, {field}, error={difference}")
        if not math.isclose(row[BOUND_FIELD], reference[BOUND_FIELD], rel_tol=1e-12, abs_tol=1e-20):
            raise AssertionError(f"Analytic tail-bound reference differs at {key}.")
    return largest_difference


def reference_payload(rows):
    return {
        "scope": "Uniform-input achievable coherent information, not optimized capacity",
        "infinite_bath_prelog": float(1.0 - np.log(2.0) / np.log(3.0)),
        "infinite_product_truncation_spins": INFINITE_PRODUCT_SPINS,
        "max_infinite_product_entropy_error_bound_bits": max(row[BOUND_FIELD] for row in rows),
        "largest_trace_error": max(row["trace_error"] for row in rows),
        "smallest_eigenvalue": min(row["minimum_computed_eigenvalue"] for row in rows),
        "rows": rows,
    }


def write_reference(rows):
    JSON_REFERENCE.write_text(json.dumps(reference_payload(rows), indent=2) + "\n")
    with CSV_REFERENCE.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-reference",
        action="store_true",
        help="explicitly replace both committed reference-data files with this run",
    )
    arguments = parser.parse_args()
    rows = compute_suite()
    endpoints = check_exact_endpoints()
    if arguments.write_reference:
        write_reference(rows)
        difference = 0.0
        action = "WROTE reference files by explicit request"
    else:
        difference = compare_reference(rows, load_reference())
        action = "PASS: reference files checked and left unchanged"

    print(action)
    print(f"Python {platform.python_version()}; NumPy {np.__version__}; SciPy {scipy.__version__}")
    print(f"Rows checked: {len(rows)}; exact endpoints checked: {len(endpoints) - 1}")
    print(f"Rate/entropy absolute tolerance: {RATE_ABSOLUTE_TOLERANCE:.1e} bits; relative tolerance: 0")
    print(f"Largest rate/entropy deviation from reference: {difference:.6g} bits")
    print(f"Infinite product: {INFINITE_PRODUCT_SPINS} retained spins")
    print(f"Largest analytic infinite-tail entropy bound: {max(row[BOUND_FIELD] for row in rows):.12g} bits")
    print(f"Largest floating-point trace error: {max(row['trace_error'] for row in rows):.12g}")
    print(f"Smallest computed eigenvalue: {min(row['minimum_computed_eigenvalue'] for row in rows):.12g}")
    print(f"Floating-point gates: min eigenvalue >= -{PSD_TOLERANCE:.1e}; trace error <= {TRACE_TOLERANCE:.1e}")
    print(f"Entropy eigenvalue cutoff: {EIGENVALUE_CUTOFF:.1e}")
    print(f"Identity endpoint rate error: {endpoints['identity_rate_error_bits']:.12g} bits")
    print(f"Uniform cyclic endpoint rate error: {endpoints['uniform_cyclic_rate_error_bits']:.12g} bits")
    print("Scope: flat-input achievable rates; no numerical optimization of capacity.")
    print("The analytic tail bound excludes floating-point error; diagnostics are not interval certification.")


if __name__ == "__main__":
    main()
