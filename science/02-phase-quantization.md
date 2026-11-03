# Phase quantization with a constant entropy error

Resolving a random phase into as many bins as there are available number states changes coherent information by at most a universal constant. The statement holds for every input distribution on those number states and every Borel phase law. This input-uniform estimate is the step that permits a converse for optimized communication.

The proof uses the established entangling-rate bound for a product Hamiltonian. The entropy comparison, its application to phase quantization, and the resulting cutoff-capacity estimate are developed below. The passage from a cutoff to a mean-energy constraint is made in the [capacity theorem](03-capacity.md).

## 1. Statement and conventions

Let $`\mu`$ be a Borel probability measure on the circle, represented on $`[0,2\pi)`$. On the Fock subspace

```math
\mathcal H_d=\mathrm{span}\{|0\rangle,\ldots,|d-1\rangle\},
```

consider the channel

```math
\mathcal N_\mu(\rho)
=\int e^{-i\theta N}\rho e^{i\theta N}\,\mu(d\theta),
\qquad N|n\rangle=n|n\rangle.
\qquad\text{(P1)}
```

All logarithms are base two. For a probability vector $`p=(p_0,\ldots,p_{d-1})`$, write $`\rho_p=\sum_np_n|n\rangle\langle n|`$ and abbreviate its coherent information as

```math
I_\mu(p)
=H(p)-S\!\left(\sum_{n<d}p_n|e_n\rangle\langle e_n|\right),
\qquad e_n(\theta)=e^{-in\theta}\in L^2(\mu).
\qquad\text{(P2)}
```

The environment vectors have unit norm. This isometry realizes the channel and its complement, including when $`\mu`$ has atoms or is singular continuous.

Partition the circle into the half-open bins

```math
J_j=\left[\frac{2\pi j}{d},\frac{2\pi(j+1)}d\right),
\quad q_j=\mu(J_j),\quad
H_d(\mu)=H(q),\quad
D_d(\mu)=\log d-H_d(\mu).
\qquad\text{(P3)}
```

The half-open convention fixes the assignment of atoms at bin boundaries. Let $`u_d`$ denote the uniform probability vector on $`0,\ldots,d-1`$, and let

```math
Q_\mu^{[d]}=\max_{p\text{ on }\{0,\ldots,d-1\}}I_\mu(p).
\qquad\text{(P4)}
```

As explained in the [model and capacity reduction](01-model.md), generalized dephasing is degradable, and a number-diagonal input is optimal. Thus (P4) is the ordinary quantum capacity when every input is restricted to this subspace. It is not the capacity under a mean-energy constraint.

Define the numerical constants

```math
\begin{aligned}
\alpha
&=2\max_{0<x<1}\sqrt{x(1-x)}
 \left|\log\frac{x}{1-x}\right|
=1.91227328893\ldots,\\
C_d&=\frac{\pi\alpha}{2}\left(1-\frac1d\right),
\qquad
C=\frac{\pi\alpha}{2}=3.00379185809\ldots .
\end{aligned}
\qquad\text{(P5)}
```

### Theorem P1: cutoff capacity and a flat input

For every $`d\ge1`$ and every Borel probability measure $`\mu`$,

```math
\boxed{
D_d(\mu)-C_d
\le I_\mu(u_d)
\le Q_\mu^{[d]}
\le D_d(\mu)+C_d .
}
\qquad\text{(P6)}
```

There is also an input-uniform comparison. Replace each phase in $`J_j`$ by the midpoint

```math
\phi_j=\frac{(2j+1)\pi}{d},
\qquad
\nu_d=\sum_{j=0}^{d-1}q_j\delta_{\phi_j}.
\qquad\text{(P7)}
```

Then, for every cutoff-supported $`p`$,

```math
\boxed{|I_\mu(p)-I_{\nu_d}(p)|\le C_d.}
\qquad\text{(P8)}
```

No regularity, density, Fourier-decay, or entropy-dimension assumption is used. The constants are independent of the phase law and input distribution.

## 2. Product-Hamiltonian entropy change

The needed inequality is an established result about entanglement generation by a product Hamiltonian. Childs, Leung, and Vidal [CLV] express its exact entanglement capacity through the spectral diameters of its two factors. The bound below is the part used here; the short proof makes its independence of Hilbert-space dimension explicit.

### Lemma P2: entropy rate

Let $`A`$ and $`B`$ be bounded Hermitian operators, and let a pure bipartite state evolve as

```math
|\Psi(t)\rangle=e^{-itA\otimes B}|\Psi(0)\rangle.
```

When one local Hilbert space is finite dimensional,

```math
\left|\frac{d}{dt}S(\Psi_A(t))\right|
\le\alpha\|A\|\,\|B\|,
\qquad\text{(P9)}
```

with the derivative understood by its continuous extension at zero eigenvalues. In particular,

```math
|S(\Psi_A(t))-S(\Psi_A(0))|
\le |t|\alpha\|A\|\,\|B\|.
\qquad\text{(P10)}
```

**Proof.** At a time with positive nonzero Schmidt coefficients, choose Schmidt bases so that

```math
|\Psi\rangle=\sum_i\sqrt{\lambda_i}|a_i\rangle|b_i\rangle.
```

Differentiating the reduced state and pairing the terms with indices $`(i,j)`$ and $`(j,i)`$ bounds the absolute entropy derivative by

```math
\sum_{i,j}\sqrt{\lambda_i\lambda_j}
\left|\log\frac{\lambda_i}{\lambda_j}\right|
|A_{ij}|\,|B_{ij}|,
\qquad\text{(P11)}
```

where $`A_{ij}=\langle a_i|A|a_j\rangle`$ and $`B_{ij}=\langle b_i|B|b_j\rangle`$. The definition of $`\alpha`$, applied to $`x=\lambda_i/(\lambda_i+\lambda_j)`$, gives

```math
\sqrt{\lambda_i\lambda_j}
\left|\log\frac{\lambda_i}{\lambda_j}\right|
\le\frac\alpha2(\lambda_i+\lambda_j).
\qquad\text{(P12)}
```

For every row,

```math
\sum_j|A_{ij}|\,|B_{ij}|
\le
\left(\sum_j|A_{ij}|^2\right)^{1/2}
\left(\sum_j|B_{ij}|^2\right)^{1/2}
\le\|A\|\,\|B\|.
\qquad\text{(P13)}
```

The same bound holds for columns. Substituting (P12) into (P11), and using $`\sum_i\lambda_i=1`$, proves (P9).

This argument also covers an infinite-dimensional second system. Schmidt rank never exceeds the dimension of the finite system, and the row and column estimates use compressions of bounded operators. The reduced finite-dimensional matrix is analytic in time under a bounded generator. A nonnegative eigenvalue that vanishes at an isolated time has an even-order zero, so its contribution to the derivative of $`-\lambda\log\lambda`$ has a removable limit there. Eigenvalues that vanish identically contribute zero. The rate bound therefore integrates to (P10). One may alternatively approximate $`B`$ by finite spectral partitions and pass to the limit using entropy continuity on the fixed finite system. $`\square`$

Adding a scalar multiple of the identity to either factor changes the evolution only by local unitaries and a phase. Thus the factors may be centered before applying (P10). For a finite spectrum, this replaces the operator norm by half the spectral diameter, in agreement with [CLV].

## 3. Compare the two phase environments on one Hilbert space

Let $`J(\theta)`$ be the bin containing $`\theta`$, and define the bounded multiplication operator

```math
R(\theta)=\theta-\phi_{J(\theta)},
\qquad |R(\theta)|\le\frac\pi d.
\qquad\text{(P14)}
```

Introduce an auxiliary label system $`C\simeq\mathcal H_d`$ and an environment $`F=L^2(\mu)`$. The two complementary states can be purified on the same space $`C\otimes F`$. Set

```math
\begin{aligned}
|\Psi_0\rangle_{CF}
&=\sum_{n<d}\sqrt{p_n}|n\rangle_C\otimes|f_n\rangle_F,
& f_n(\theta)&=e^{-in\phi_{J(\theta)}},\\
|\Psi_1\rangle_{CF}
&=\sum_{n<d}\sqrt{p_n}|n\rangle_C\otimes|e_n\rangle_F,
& e_n(\theta)&=e^{-in\theta}.
\end{aligned}
\qquad\text{(P15)}
```

The vectors $`f_n`$ have the same Gram matrix as environment vectors for $`\nu_d`$, because integration over a bin contributes its probability $`q_j`$. The two $`F`$-marginals therefore have exactly the complementary-output entropies appearing in (P8). Since the purifications are pure, their $`C`$-marginals have those same entropies. These $`C`$-marginals are Gram matrices; they are not the physical receiver outputs for the number-diagonal input. Those outputs remain $`\rho_p`$.

The relation between these purifications is particularly simple:

```math
|\Psi_1\rangle=e^{-iN_C\otimes R}|\Psi_0\rangle.
\qquad\text{(P16)}
```

Center the number operator on the cutoff subspace,

```math
A=N_C-\frac{d-1}{2}I,
\qquad \|A\|=\frac{d-1}{2}.
```

The term removed from $`N_C`$ generates only a local bath unitary. Equations (P10) and (P14) consequently imply

```math
\begin{aligned}
|S(\Psi_{1,C})-S(\Psi_{0,C})|
&\le\alpha\frac{d-1}{2}\frac\pi d\\
&=C_d.
\end{aligned}
\qquad\text{(P17)}
```

For a number-diagonal input, the receiver output is $`\rho_p`$ under both channels. Its entropy is the same $`H(p)`$. Only the complementary entropy changes, so (P17) proves (P8).

The estimate controls entropy directly. It does not require the two channels to become close in unrestricted diamond norm as $`d`$ grows. A phase residual of order $`1/d`$ acting across a number range of order $`d`$ has a bounded product-Hamiltonian entangling strength, which is precisely the quantity entering this proof.

## 4. The rounded channel is exactly solvable

Let

```math
Z_d=\sum_{n=0}^{d-1}e^{-2\pi in/d}|n\rangle\langle n|,
\qquad U_0=e^{-i\pi N/d}.
```

The rounded channel is

```math
\mathcal N_{\nu_d}(\rho)
=U_0\left(\sum_{j=0}^{d-1}q_jZ_d^j\rho Z_d^{-j}\right)U_0^\dagger.
\qquad\text{(P18)}
```

The common output unitary $`U_0`$ has no effect on coherent information. The channel in parentheses is finite-dimensional cyclic dephasing. Like every generalized-dephasing channel, it is degradable, so coherent information is concave in the input. It is covariant under the discrete Weyl operators: phase shifts commute with its errors, and cyclic number shifts commute with them up to scalar phases. Coherent information is invariant under these input conjugations. Averaging any input over the Weyl group gives $`I_d/d`$; concavity therefore makes this maximally mixed input optimal.

At $`I_d/d`$, the receiver entropy is $`\log d`$. Applying the phase errors to half of a maximally entangled state gives the orthogonal vectors

```math
(I\otimes Z_d^j)|\Phi_d\rangle,
\qquad
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{n=0}^{d-1}|n,n\rangle.
```

Their mixture has eigenvalues $`q_j`$. The complementary entropy is consequently $`H(q)`$, and

```math
\max_p I_{\nu_d}(p)
=I_{\nu_d}(u_d)
=\log d-H(q)
=D_d(\mu).
\qquad\text{(P19)}
```

For any $`p`$, (P8) and (P19) give $`I_\mu(p)\le D_d+C_d`$. Applying (P8) to $`u_d`$ gives the matching lower estimate. This proves Theorem P1. When $`d=1`$, both coherent informations and $`D_d`$ vanish, and $`C_d=0`$, so the statement includes that case exactly.

## 5. Toeplitz entropy and the role of earlier spectral results

For the flat input, define the normalized Toeplitz matrix

```math
\tau_d=\frac1dT_d(\mu),
\qquad
(T_d(\mu))_{nm}
=\int e^{-i(n-m)\theta}\,\mu(d\theta),
\quad 0\le n,m<d.
\qquad\text{(P20)}
```

It is the output of $`\mathcal N_\mu`$ on the uniform number superposition. Its nonzero spectrum is also that of the complementary output for $`u_d`$. Equation (P17), evaluated at that input, gives

```math
\boxed{|S(\tau_d)-H_d(\mu)|\le C_d.}
\qquad\text{(P21)}
```

The interpretation of a flat-input entropy through spectral dimension has an important antecedent. Guarneri [G] studies the entropy of a time-averaged quantum orbit. The orbit state is isospectral to a Toeplitz state of the form (P20), and regular spectral measures yield a dimension-dependent logarithmic entropy law. The present argument uses a comparison that is uniform over arbitrary cutoff input distributions, as required by the optimized converse. The dimension-free entangling-rate inequality itself is inherited from [CLV].

## Sources

**[CLV]** A. M. Childs, D. W. Leung, and G. Vidal, *Reversible simulation of bipartite product Hamiltonians*, IEEE Transactions on Information Theory **50**, 1189–1197 (2004). [Primary manuscript, arXiv:quant-ph/0303097](https://arxiv.org/pdf/quant-ph/0303097), especially equation (6) and Section IV. This is the source for the product-Hamiltonian entanglement-capacity bound, including the constant $`\alpha`$.

**[G]** I. Guarneri, *On the Dynamical Meaning of Spectral Dimensions*, [primary manuscript, arXiv:math-ph/9804009](https://arxiv.org/pdf/math-ph/9804009) (1998), especially Theorem 1. This supplies the earlier spectral-dimension interpretation of the entropy of a prescribed time-averaged state.

The [model](01-model.md) and [capacity theorem](03-capacity.md) identify the separate coding-theorem and energy-constraint ingredients.
