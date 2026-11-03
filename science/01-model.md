# The channel, energy budget and coding problem

[Science route](README.md) · Next: [phase quantization](02-phase-quantization.md)

## Why finite energy changes the question

An oscillator can carry information in coherence between photon-number states. A random phase rotation leaves every photon-number probability unchanged, while suppressing selected off-diagonal matrix elements. Increasing the available photon number gives access to finer angular structure in the noise. The question is how much of that structure a communication protocol can use when only its mean photon number is bounded.

The phase law may have atoms, a density, a singular continuous part, or a mixture of these. The result concerns all such laws. It compares the optimal quantum communication rate with one classical quantity: the entropy of the noise after angular binning at the resolution set by the energy budget.

## Channel and phase convention

Let the oscillator Hilbert space be $`\ell^2(\mathbb N_0)`$, with photon-number operator

```math
N=\sum_{n=0}^{\infty}n|n\rangle\langle n|.
```

Let $`\mu`$ be a Borel probability measure on the circle, represented on the half-open interval $`[0,2\pi)`$. The channel is

```math
\mathcal N_\mu(\rho)
=\int_{[0,2\pi)}e^{-i\theta N}\rho e^{i\theta N}\,\mu(d\theta).
\qquad\text{(1.1)}
```

The integral defines a normal quantum channel, including when the measure has no density. Its number-basis action is

```math
\langle n|\mathcal N_\mu(\rho)|k\rangle
=\widehat\mu(n-k)\rho_{nk},
\qquad
\widehat\mu(j)=\int e^{-ij\theta}\,\mu(d\theta).
\qquad\text{(1.2)}
```

Each channel use samples an independent phase from the same known law. Neither sender nor receiver receives the sampled phase. Independent uses are essential: reusing a single static environment produces a memory channel and is a different communication problem.

## The charged resource

For a block of $`\ell`$ channel uses, define the mean photon-number observable

```math
\overline N_\ell
=\frac1\ell\sum_{j=1}^{\ell}N_j.
\qquad\text{(1.3)}
```

An entanglement-transmission code has a logical system of dimension $`M_\ell`$, an encoder $`\mathcal E_\ell`$ and a decoder. Its encoded maximally mixed logical state must obey

```math
\mathrm{Tr}\!\left[
\overline N_\ell\,
\mathcal E_\ell\!\left(\frac{I_{M_\ell}}{M_\ell}\right)
\right]\le E.
\qquad\text{(1.4)}
```

The entanglement-transmission error tends to zero as the block length grows. The capacity $`Q_\mu(E)`$ is the supremum of achievable rates $`\liminf_{\ell\to\infty}\ell^{-1}\log_2 M_\ell`$, in qubits per use. This is an unconditional average input-energy constraint, averaged across channel uses. It permits rare high-photon components and does not impose a hard photon cutoff.

Arbitrary encoders, decoders and local ancillas are allowed, without shared entanglement or assistance from a classical communication channel. The resource being bounded is the channel input's mean photon number. No bound on the computational complexity or thermodynamic cost of encoding and decoding is asserted. The channel is pure dephasing; photon loss is not included.

## An arbitrary-measure dilation

The environment may be taken to be $`L^2(\mu)`$. Define unit vectors

```math
e_n(\theta)=e^{-in\theta},
\qquad
V|n\rangle=|n\rangle\otimes|e_n\rangle.
\qquad\text{(1.5)}
```

The orthogonality of the oscillator basis makes $`V`$ an isometry, even though the environment vectors need not be orthogonal. Tracing out the environment gives (1.1), and tracing out the oscillator gives

```math
\mathcal N_\mu^c(\rho)
=\sum_{n=0}^{\infty}\rho_{nn}|e_n\rangle\langle e_n|.
\qquad\text{(1.6)}
```

Measuring the receiver in the number basis and preparing $`|e_n\rangle`$ simulates the complementary channel. Thus $`\mathcal N_\mu`$ is degradable for every Borel measure. This argument does not require a finite-dimensional environment or a phase density.

Write $`p_n=\rho_{nn}`$. The channel preserves these probabilities. Dephasing its output completely in the number basis raises entropy, while (1.6) is unchanged. Consequently a Fock-diagonal input is optimal for coherent information at fixed $`p`$:

```math
I_c(p,\mathcal N_\mu)
=H(p)-S\!\left(\sum_n p_n|e_n\rangle\langle e_n|\right).
\qquad\text{(1.7)}
```

## Why the single-letter formula is valid here

The energy-constrained coding theorem for degradable channels gives

```math
Q_\mu(E)
=\sup_{\substack{p_n\ge0,\ \sum_n p_n=1\\
                  \sum_n n p_n\le E}}
I_c(p,\mathcal N_\mu).
\qquad\text{(1.8)}
```

The relevant general result is [Wilde–Qi, Theorem 3](https://arxiv.org/abs/1609.01997), with the average-energy entanglement-transmission convention in their Section III and its equivalence result, Theorem 1. Its assumptions can be checked directly in the present model.

For every positive $`\beta`$,

```math
\mathrm{Tr}e^{-\beta N}=(1-e^{-\beta})^{-1}\lt\infty.
\qquad\text{(1.9)}
```

Thus $`N`$ is a Gibbs observable. A number distribution of mean at most $`E`$ has entropy at most the geometric-distribution entropy

```math
g(E)=(E+1)\log_2(E+1)-E\log_2 E.
\qquad\text{(1.10)}
```

The output entropy is at most $`H(p)\le g(E)`$, because number dephasing increases entropy. The complementary output is a pure-state ensemble with weights $`p`$, so its entropy is also at most $`H(p)`$. These bounds ensure that the entropies in (1.7) are finite and verify the theorem's finite-output-entropy hypothesis. Degradability was proved above.

The formula is inherited channel theory, not the new capacity estimate. Its role is to identify the optimization that the [constant-error theorem](03-capacity.md) evaluates. Concavity of coherent information and its subadditivity for degradable channels are what prevent entangled block inputs or uneven energy allocation between uses from improving that single-letter optimum.

## Angular entropy at a finite resolution

For an integer $`m\ge1`$, use the fixed half-open bins

```math
B_j^{(m)}=[2\pi j/m,2\pi(j+1)/m),
\qquad j=0,\ldots,m-1.
```

Their probabilities and entropy are

```math
q_j^{(m)}=\mu(B_j^{(m)}),
\qquad
H_m(\mu)=-\sum_{j=0}^{m-1}q_j^{(m)}\log_2 q_j^{(m)}.
\qquad\text{(1.11)}
```

The convention $`0\log_2 0=0`$ handles empty bins. Define

```math
D_m(\mu)=\log_2m-H_m(\mu)
=D\!\left(q^{(m)}\middle\|u_m\right),
\qquad\text{(1.12)}
```

where $`u_m`$ is the uniform classical distribution on the bins. Hence $`0\le D_m\le\log_2m`$. All binning statements include atoms at bin boundaries under the stated half-open convention. The proof does not assume smoothness or Fourier decay.

The theorem connects this classical angular entropy deficit to the optimized quantum communication rate. The phase-bin origin is a convention: changing it can change the histogram entropy by at most one bit, which does not affect the universal bounded-error statement.

## Reading onward

[Phase quantization](02-phase-quantization.md) explains why a grid at resolution $`1/d`$ approximates every input supported on $`d`$ consecutive number states with a bounded entropy error. [The capacity theorem](03-capacity.md) then handles the unrestricted photon-number tail under (1.4). [The physical examples](04-bath-and-smoothing.md) distinguish finite baths, infinite geometric baths and continuous background broadening.
