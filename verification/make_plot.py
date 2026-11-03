#!/usr/bin/env python3
"""Plot the six committed flat-input curves; no diagonalizations are performed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


DIRECTORY = Path(__file__).resolve().parent


def make_figure(rows):
    """Build the two-panel figure from already checked reference rows."""
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "svg.fonttype": "path",
            "svg.hashsalt": "bosonic-phase-noise-capacity",
        }
    )
    figure, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), sharex=True, sharey=True)
    styles = {
        3: ("#1d5a91", "o", "3 bath spins"),
        6: ("#c26a1b", "s", "6 bath spins"),
        "infinite": ("#7650a1", "^", "Infinite bath"),
    }
    for axis, sigma in zip(axes, (0.0, 0.02), strict=True):
        for bath_spins, (color, marker, label) in styles.items():
            selected = sorted(
                (
                    row
                    for row in rows
                    if row["bath_spins"] == bath_spins
                    and row["gaussian_sigma_radians"] == sigma
                ),
                key=lambda row: row["d"],
            )
            axis.plot(
                [np.log2(row["d"]) for row in selected],
                [row["flat_input_coherent_information_bits"] for row in selected],
                color=color,
                marker=marker,
                markersize=5,
                linewidth=2,
                label=label,
            )
        axis.set_xticks([5, 6, 7, 8, 9])
        axis.set_xlim(4.85, 9.15)
        axis.set_ylim(0, 6.35)
        axis.set_xlabel(r"Number cutoff, $\log_2 d$")
        axis.grid(axis="y", color="#d9e0e7", linewidth=0.7)
        axis.set_axisbelow(True)
    axes[0].set_ylabel("Achievable qubits per channel use")
    axes[0].set_title("No added Gaussian phase noise", loc="left", fontsize=11, pad=12)
    axes[1].set_title(r"Gaussian phase width $\sigma=0.02$ rad", loc="left", fontsize=11, pad=12)
    axes[0].legend(frameon=False, loc="upper left")
    figure.suptitle("Flat-number input: six achievable-rate curves", x=0.075, ha="left", fontsize=14)
    figure.text(
        0.075,
        0.055,
        "Mean photons = (d - 1)/2. These are coherent-information rates, not optimized capacities.",
        fontsize=9,
        color="#394957",
    )
    figure.tight_layout(rect=(0.025, 0.10, 0.995, 0.91), w_pad=2.0)
    return figure


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DIRECTORY / "flat-input-rates.svg")
    arguments = parser.parse_args()
    rows = json.loads((DIRECTORY / "reference-data.json").read_text())["rows"]
    figure = make_figure(rows)
    figure.savefig(
        arguments.output,
        format="svg",
        metadata={
            "Title": "Flat-number achievable rates for geometric phase baths",
            "Description": (
                "Two panels show the six committed uniform-input coherent-information curves. "
                "They are achievable rates, not optimized capacities. The infinite product is "
                "truncated at 18 spins with an analytic entropy-error bound; floating-point "
                "eigensolver diagnostics are separate and are not interval certificates."
            ),
            "Date": None,
        },
    )
    plt.close(figure)
    print(f"Wrote {arguments.output}")


if __name__ == "__main__":
    main()
