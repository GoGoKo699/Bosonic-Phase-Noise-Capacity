# Two phases, two encodings

[Learning route](README.md) · [Anchor and source bridge](anchor.md) · [Milestone map](milestones.md)

Consider an oscillator that receives either no phase rotation or a half-turn, each with probability one half. The sender and receiver know these probabilities but do not learn which rotation occurred. Different uses draw their rotations independently. This small example shows what the channel changes, why the choice of photon levels matters, and how a complementary entropy enters an achievable quantum rate.

## 1. What the noise does

The photon-number state $`|n\rangle`$ has exactly $`n`$ photons. A half-turn multiplies it by $`e^{-i\pi n}=(-1)^n`$: even number states keep their sign, and odd number states change sign. The phase law and channel are

```math
\mu=\tfrac12\delta_0+\tfrac12\delta_\pi,
\qquad
\mathcal N_\mu(\rho)
=\tfrac12\rho+\tfrac12 e^{-i\pi N}\rho e^{i\pi N}.
```

Here $`\delta_\theta`$ means a distribution concentrated at phase $`\theta`$. Averaging the two rotations gives

```math
\langle n|\mathcal N_\mu(\rho)|k\rangle
=\frac{1+(-1)^{n-k}}2\rho_{nk}.
```

Thus coherence between states of the same parity survives. Coherence between even and odd states vanishes. The diagonal number probabilities remain unchanged in both cases. This is the [channel's Fourier rule](../science/01-model.md#channel-and-phase-convention) in an exactly calculable example.

## 2. The encoding determines which coherence matters

Let $`a|0\rangle+b|1\rangle`$ encode an unknown qubit, with $`|a|^2+|b|^2=1`$. The half-turn changes the relative sign of its two amplitudes. The averaged output is

```math
|a|^2|0\rangle\langle0|
+|b|^2|1\rangle\langle1|.
```

The input's relative phase has disappeared. The receiver cannot reconstruct an arbitrary unknown qubit from these two probabilities.

Instead encode the same logical amplitudes as $`a|0\rangle+b|2\rangle`$. Both occupied levels are even, so either rotation leaves the state unchanged. A decoder that maps levels zero and two back to the logical qubit recovers it exactly. This encoding also preserves entanglement with an untouched reference system, because the channel acts as the identity on the entire two-dimensional subspace.

| Encoding | Effect of either allowed rotation | Largest mean photon number over logical inputs |
|---|---|---:|
| Levels 0 and 1 | Their relative sign may change | 1 |
| Levels 0 and 2 | Their relative phase is preserved | 2 |

For the second encoding, the charged mean photon number is $`2|b|^2`$. Its encoded maximally mixed logical input has mean one photon. The example exposes a real tradeoff: choosing a larger number separation can avoid this particular phase noise, and that choice has an energy cost. The project's [capacity convention](../science/01-model.md#the-charged-resource) specifies the unconditional encoded-input mean averaged across a communication block.

## 3. An exact coherent-information calculation

Now take a different input: the uniform mixture on the first four levels,

```math
\rho_{u_4}=\frac14\sum_{n=0}^{3}|n\rangle\langle n|,
\qquad
\mathrm{Tr}(N\rho_{u_4})=\frac32.
```

The physical receiver output is still $`\rho_{u_4}`$, with entropy two bits. For the complement, use a two-dimensional environment with orthonormal basis $`|0\rangle_F,|1\rangle_F`$. The dilation associates an even photon number with one state and an odd photon number with an orthogonal state:

```math
|e_{\mathrm{even}}\rangle
=\frac{|0\rangle_F+|1\rangle_F}{\sqrt2},
\qquad
|e_{\mathrm{odd}}\rangle
=\frac{|0\rangle_F-|1\rangle_F}{\sqrt2}.
```

The environment records parity but cannot distinguish the two even levels from one another, or the two odd levels from one another. Since each parity occurs with probability one half, its state has two eigenvalues equal to one half and entropy one bit. Therefore

```math
I_c(u_4,\mathcal N_\mu)
=S(\mathcal N_\mu(\rho_{u_4}))
 -S(\mathcal N_\mu^c(\rho_{u_4}))
=2-1=1.
```

Coherent-information coding makes this an achievable rate of one qubit per use at a mean photon budget of $`3/2`$. This rate statement concerns transmitting a purification over many independent uses; it does not mean that sending classical number labels transmits qubits. The explicit two-level encoding above and this four-level input calculation are two ways to see surviving quantum information, with their own input energies.

The physical receiver has entropy two, while the environment has entropy one. A finite Gram matrix used to compute the latter has the environment's nonzero spectrum. It is an auxiliary representation, not the physical receiver output. This is the distinction used in the [common-purification proof](../science/02-phase-quantization.md#3-compare-the-two-phase-environments-on-one-hilbert-space).

## 4. What the phase histogram predicts

Divide the phase circle into four equal half-open bins. Only the bins containing zero and $`\pi`$ are occupied, so their probabilities are one half each. Thus

```math
H_4(\mu)=1,
\qquad
D_4(\mu)=\log_2 4-H_4(\mu)=1.
```

Here the four-level achievable rate equals the histogram deficit exactly. For a general phase law, the project proves that the cutoff comparison has a uniformly bounded error. It then controls all higher photon levels allowed by a mean constraint. The example's cutoff $`d=4`$ and mean energy $`E=3/2`$ are different quantities; they should not be substituted for each other in the mean-energy theorem's choice $`m=\lceil E\rceil`$.

This two-point law has $`H_m(\mu)=1`$ for every integer $`m\ge2`$. The [general theorem](../science/03-capacity.md#main-theorem) consequently gives logarithmic high-energy capacity growth with a fixed entropy deficit, up to its universal additive error. A law with structure on ever finer scales can keep adding histogram entropy as energy increases. The [bath and smoothing analysis](../science/04-bath-and-smoothing.md) explains how a finite bath and continuous background broadening change that process.

The example supports M01–M09: carrier, random phase, composite states, complementary output and coherent information. M15–M21 explain why the histogram comparison extends beyond a solvable example to an optimized bound for every admissible input.
