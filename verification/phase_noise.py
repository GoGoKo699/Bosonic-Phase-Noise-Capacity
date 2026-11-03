"""Flat-input coherent information for the finite geometric spin-bath examples.

The functions evaluate the prescribed flat number input, not the capacity
optimization. Gaussian widths are in radians; all entropies use bits.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.linalg import eigvalsh, toeplitz


INFINITE_PRODUCT_SPINS = 18
DIMENSIONS = (32, 64, 128, 256, 512)
BATH_SIZES = (3, 6, "infinite")
GAUSSIAN_WIDTHS = (0.0, 0.02)
EIGENVALUE_CUTOFF = 1e-15
PSD_TOLERANCE = 1e-11
TRACE_TOLERANCE = 1e-10
RATE_ABSOLUTE_TOLERANCE = 1e-9


def binary_entropy(probability: float) -> float:
    """Binary Shannon entropy, including its continuous endpoint values."""
    if probability <= 0.0 or probability >= 1.0:
        return 0.0
    return float(
        -probability * np.log2(probability)
        - (1.0 - probability) * np.log2(1.0 - probability)
    )


def bath_characteristic(
    dimension: int,
    bath_spins: int | str,
    sigma_radians: float,
    infinite_product_spins: int = INFINITE_PRODUCT_SPINS,
) -> np.ndarray:
    """Return the characteristic function at integer differences 0,...,d-1.

    Each fair spin contributes a phase +/- 2*pi*3**(-k). This centered
    convention differs from the {0, 2} Cantor convention by a known rotation,
    which leaves the Toeplitz entropy unchanged.
    """
    last_spin = infinite_product_spins if bath_spins == "infinite" else int(bath_spins)
    differences = np.arange(dimension, dtype=float)
    characteristic = np.ones(dimension)
    for spin in range(1, last_spin + 1):
        characteristic *= np.cos(2.0 * np.pi * differences / 3**spin)
    characteristic *= np.exp(-0.5 * sigma_radians**2 * differences**2)
    return characteristic


def discrete_phase_characteristic(
    dimension: int,
    phases_radians: np.ndarray,
    probabilities: np.ndarray,
) -> np.ndarray:
    """Characteristic function for a specified finite phase law."""
    differences = np.arange(dimension, dtype=float)
    return np.exp(-1j * np.outer(differences, phases_radians)) @ probabilities


def entropy_diagnostics(characteristic: np.ndarray) -> dict[str, float]:
    """Diagonalize T_d/d and return entropy plus floating-point diagnostics.

    Eigenvalues at or below 1e-15 do not contribute to the entropy sum.
    This is a stated floating-point convention, not an interval certificate.
    """
    dimension = len(characteristic)
    state = toeplitz(characteristic) / dimension
    eigenvalues = eigvalsh(state)
    minimum_eigenvalue = float(eigenvalues[0])
    trace_error = abs(float(eigenvalues.sum()) - 1.0)
    if minimum_eigenvalue < -PSD_TOLERANCE:
        raise AssertionError(f"PSD diagnostic failed: min eigenvalue={minimum_eigenvalue}")
    if trace_error > TRACE_TOLERANCE:
        raise AssertionError(f"Trace diagnostic failed: error={trace_error}")
    positive = eigenvalues[eigenvalues > EIGENVALUE_CUTOFF]
    entropy = float(-np.dot(positive, np.log2(positive)))
    return {
        "environment_entropy_bits": entropy,
        "flat_input_coherent_information_bits": float(np.log2(dimension) - entropy),
        "minimum_computed_eigenvalue": minimum_eigenvalue,
        "trace_error": trace_error,
    }


def infinite_product_entropy_bound(
    dimension: int, retained_spins: int = INFINITE_PRODUCT_SPINS
) -> float:
    """Analytic truncation error in entropy; excludes floating-point error.

    |1 - product_{k>L} cos(2*pi*l/3**k)| <= pi**2*l**2/(4*9**L).
    The normalized matrix Frobenius bound and rank d give half trace distance
    at most sqrt(d)/2 times this coefficient bound. Audenaert's inequality
    then bounds entropy difference. If the distance bound exceeds the
    monotonicity range, the trivial log2(d) entropy bound is used instead.
    """
    if dimension <= 1:
        return 0.0
    coefficient_bound = np.pi**2 * (dimension - 1) ** 2 / (4.0 * 9.0**retained_spins)
    half_trace_bound = math.sqrt(dimension) * coefficient_bound / 2.0
    if half_trace_bound >= 1.0 - 1.0 / dimension:
        return math.log2(dimension)
    return float(
        half_trace_bound * np.log2(dimension - 1) + binary_entropy(half_trace_bound)
    )


def flat_input_result(
    dimension: int, bath_spins: int | str, sigma_radians: float
) -> dict[str, int | str | float]:
    """One row of the published 30-point suite."""
    diagnostics = entropy_diagnostics(
        bath_characteristic(dimension, bath_spins, sigma_radians)
    )
    rate = diagnostics["flat_input_coherent_information_bits"]
    return {
        "d": dimension,
        "mean_photons": (dimension - 1) / 2.0,
        "bath_spins": bath_spins,
        "gaussian_sigma_radians": sigma_radians,
        "environment_entropy_bits": diagnostics["environment_entropy_bits"],
        "flat_input_coherent_information_bits": rate,
        "coherent_information_over_log2_d": rate / np.log2(dimension),
        "infinite_product_entropy_error_bound_bits": (
            infinite_product_entropy_bound(dimension)
            if bath_spins == "infinite"
            else 0.0
        ),
        "minimum_computed_eigenvalue": diagnostics["minimum_computed_eigenvalue"],
        "trace_error": diagnostics["trace_error"],
    }


def compute_suite() -> list[dict[str, int | str | float]]:
    """Recompute exactly the six curves at their five existing cutoffs."""
    return [
        flat_input_result(dimension, bath_spins, sigma)
        for sigma in GAUSSIAN_WIDTHS
        for bath_spins in BATH_SIZES
        for dimension in DIMENSIONS
    ]


def check_exact_endpoints(dimension: int = 32) -> dict[str, float]:
    """Two exact channel endpoints catch normalization and phase conventions."""
    identity = entropy_diagnostics(
        discrete_phase_characteristic(dimension, np.array([0.0]), np.array([1.0]))
    )
    phases = 2.0 * np.pi * np.arange(dimension) / dimension
    uniform = entropy_diagnostics(
        discrete_phase_characteristic(dimension, phases, np.ones(dimension) / dimension)
    )
    identity_error = abs(
        identity["flat_input_coherent_information_bits"] - math.log2(dimension)
    )
    uniform_error = abs(uniform["flat_input_coherent_information_bits"])
    endpoint_tolerance = 1e-10
    if identity_error > endpoint_tolerance or uniform_error > endpoint_tolerance:
        raise AssertionError((identity_error, uniform_error, endpoint_tolerance))
    return {
        "identity_rate_error_bits": identity_error,
        "uniform_cyclic_rate_error_bits": uniform_error,
        "endpoint_absolute_tolerance_bits": endpoint_tolerance,
    }
