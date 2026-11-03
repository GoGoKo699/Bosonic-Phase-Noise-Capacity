# Meaning, comparisons and limits

[Science route](README.md) · [Main theorem](03-capacity.md) · [Physical examples](04-bath-and-smoothing.md)

## Energy sets the relevant angular resolution

An oscillator can resolve smaller phase differences by using coherence between more widely separated photon numbers. The capacity theorem gives this intuition an operational form. At mean photon number $`E`$, the classical entropy deficit of the phase histogram with about $`E`$ bins determines the best quantum communication rate within a universal additive constant.

The converse matters as much as the flat-input construction. A mean-energy constraint permits arbitrarily rare components at arbitrarily high photon number. It also permits nonuniform input distributions tailored to the noise. The shell proof bounds both possibilities. The rate estimate therefore applies to the optimized communication problem, rather than only to a selected family of probe states or encodings.

The explicit constant-gap guarantee is deliberately conservative. It identifies the leading growth and gives a noise-uniform approximation, but a gap of several qubits per use can be too coarse for a small-capacity device. Sharpening the constants is not necessary for the dimension law, and no claim of experimentally precise capacity prediction follows from them.

## Information dimension is a consequence, not an extra hypothesis

If the histogram entropy satisfies $`H_m(\mu)=d_I\log_2m+o(\log m)`$, the theorem gives $`Q_\mu(E)=(1-d_I)\log_2E+o(\log E)`$. Discrete laws, regular fractal laws and smooth laws can therefore have different leading behavior. The full histogram formula carries more information than this coefficient: it still describes irregular distributions, finite-scale transitions and sublogarithmic changes when a limiting dimension is absent or equals one.

The prior spectral-entropy result of Guarneri already reveals a related dimension law for a prescribed uniform orbit state. Classical information dimension is also long established. The optimized mean-energy comparison is the additional communication statement; it neither defines a new dimension nor makes the earlier spectral mechanism a new discovery. See the [precise comparison](../references/related-work.md#spectral-dimensions-already-control-uniform-orbit-entropy-slopes).

## The three resolution regimes of a geometric bath

For $`K`$ independent fair spins with geometrically decreasing couplings, each resolved spin supplies one bit of phase uncertainty. Before the finest relevant spin scale is resolved, the number of visible spins grows proportionally to $`\log E`$. That creates the fractional coefficient in the capacity growth.

For a fixed finite bath, the number of uncertain spin labels eventually stops growing. The capacity then has the ordinary logarithmic growth of an oscillator, with a bounded bath-entropy deficit. This differs from taking the bath size to infinity before taking energy large. The [uniform finite-bath theorem](04-bath-and-smoothing.md) makes both limits part of one finite-resolution statement.

Independent Gaussian broadening gives a second stopping scale. Once the oscillator resolves angles below the broadening width, increasing the photon budget reveals additional smooth noise entropy at the same logarithmic rate as the noiseless information budget grows. The terms cancel to bounded error, producing saturation. This is why an exact infinite-bath fractal slope is not asymptotically stable under a fixed amount of continuous broadening.

The formulas describe bounded-error growth regimes, not a pointwise derivative or a sharp transition at a unique energy. Constants depending on the geometric ratio can shift the crossover locations by fixed factors.

## What the finite calculations show

The committed calculations use Toeplitz matrices for uniform Fock inputs and display the finite-bath and smooth-noise regimes. The input width is $`d`$, so its mean photon number is exactly $`(d-1)/2`$. The numerical rate is

```math
I_c(u_d,\mathcal N_\mu)
=\log_2d-S(T_d(\mu)/d).
```

The [verification guide](../verification/README.md) gives the phase normalization, the infinite-product truncation bound and the separate floating-point checks. These values are achievable coherent-information rates. They do not evaluate the optimized capacity or numerically certify an asymptotic exponent. The full-tail converse and error constants come from the proof.

## Scope of the communication model

The phase distribution is known, but the realized phase is hidden. The theorem does not charge the sample complexity of identifying that distribution. It does charge input photons through an unconditional block-average constraint; postselection on favorable energy or noise events is not part of the definition.

The model supplies independent channel uses. In a spin-bath realization this means independently prepared or reset baths. Reset work and bath preparation are not part of the photon capacity budget. A single bath interacting with successive signals generally correlates their noise; the resulting memory-channel capacity needs a different analysis.

The channel preserves photon number. Adding photon loss can fundamentally change high-energy communication, so the phase-only law cannot be applied to a loss-dephasing channel by inserting a phase histogram. The result also does not give two-way-assisted capacities for arbitrary singular measures, a strong converse, a finite-block coding theorem with explicit errors, or an implementation of the encoder with controlled gate complexity.

These boundaries keep the operational conclusion precise: arbitrary phase laws admit a universal finite-energy capacity estimate, and a simple input spectrum is within a fixed additive gap of the optimum under the stated model.
