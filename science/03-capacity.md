# The universal capacity bound

[Science route](README.md) · Previous: [phase quantization](02-phase-quantization.md) · Next: [bath and smoothing](04-bath-and-smoothing.md)

The [model](01-model.md) reduces quantum capacity to a single coherent-information optimization. The [phase-quantization lemma](02-phase-quantization.md) solves its hard-cutoff version to a constant error. The remaining issue is substantive: a bound on mean photon number permits a distribution with arbitrarily large values of the photon number. Those values cannot simply be discarded in a converse.

## Main theorem

Let $`\mu`$ be any Borel phase law, $`E\ge1`$, and $`m=\lceil E\rceil`$. Let $`u_m`$ now denote the Fock distribution uniform on $`0,\ldots,m-1`$; its meaning as an input distribution is distinct from the bin reference distribution in the definition of $`D_m`$. Set

```math
\alpha=2\max_{0\lt x\lt1}
\sqrt{x(1-x)}\left|\log_2\frac{x}{1-x}\right|
=1.9122732889\ldots,
\qquad C=\frac{\pi\alpha}{2}=3.0037918581\ldots.
\tag{3.1}
```

**Theorem 1.** Under the unassisted, independent-use, average-energy model of the preceding page,

```math
D_m(\mu)-C
\le I_c(u_m,\mathcal N_\mu)
\le Q_\mu(E)
\le D_m(\mu)+C+3.
\tag{3.2}
```

In particular,

```math
Q_\mu(E)=\log_2 E-H_{\lceil E\rceil}(\mu)+O(1),
\tag{3.3}
```

with a constant independent of both the phase law and the energy. The constants in (3.2) are sufficient analytical bounds, not claimed optimal. They can be coarse when the capacity itself is small.

The uniform input is feasible because its mean photon number is $`(m-1)/2\le E`$. Combining the bounds shows

```math
0\le Q_\mu(E)-I_c(u_m,\mathcal N_\mu)
\le 2C+3\lt9.008.
\tag{3.4}
```

The lower bound is an achievable coding rate furnished by coherent-information coding. It is not a new efficient encoder or a finite-block error guarantee.

## The hard-cutoff input lemma

Let $`Q_\mu^{[d]}`$ denote the maximum coherent information over photon distributions supported on $`0,\ldots,d-1`$, without a separate mean constraint. The preceding page proves

```math
D_d(\mu)-C_d
\le I_c(u_d,\mathcal N_\mu)
\le Q_\mu^{[d]}
\le D_d(\mu)+C_d,
\quad
C_d=\frac{\pi\alpha}{2}\frac{d-1}{d}\le C.
\tag{3.5}
```

The stronger fact behind this inequality is uniform in the input distribution: rounding each phase to the center of one of $`d`$ bins changes its complementary entropy by at most $`C_d`$. The grid channel is a finite cyclic dephasing channel with exact capacity $`D_d`$. The product-interaction entangling-rate inequality used to obtain this statement is an established result of Childs, Leung and Vidal; its application and the full calculation are given in [the quantization proof](02-phase-quantization.md).

## A photon-number shift does not change coherent information

Suppose a distribution is supported on $`a,\ldots,a+d-1`$. Subtract $`a`$ from every occupied photon index. This does not change the Shannon entropy. In the environment representation,

```math
e_{a+n}(\theta)=e^{-ia\theta}e_n(\theta).
\tag{3.6}
```

Multiplication by $`e^{-ia\theta}`$ is one common unitary on $`L^2(\mu)`$. It conjugates the entire complementary state and therefore leaves its entropy unchanged. The original and shifted distributions have identical coherent information. The original distribution need not satisfy a new cutoff energy constraint: this observation is used only to bound it by the unrestricted cutoff optimum for a block of the same length.

## Dyadic shells control the whole energy tail

For a photon number $`n`$, define the nonnegative integer

```math
K(n)=\left\lfloor\log_2\!\left(1+\frac nm\right)\right\rfloor.
\tag{3.7}
```

Shell $`k`$ is exactly

```math
\mathcal B_k
=\{m(2^k-1),\ldots,m(2^{k+1}-1)-1\},
\qquad d_k=|\mathcal B_k|=m2^k.
\tag{3.8}
```

For any admissible photon distribution $`p`$, the pointwise relation $`2^{K(n)}\le1+n/m`$ gives

```math
\mathbb E_p[2^K]\le1+\frac Em\le2,
\qquad
\mathbb E_p[K]\le\log_2\mathbb E_p[2^K]\le1.
\tag{3.9}
```

A nonnegative integer random variable of mean at most one has entropy at most the geometric-distribution entropy at that mean. Hence

```math
H(K)\le g(\mathbb E[K])\le g(1)=2.
\tag{3.10}
```

Let $`w_k=\Pr(K=k)`$ and let $`p^{(k)}`$ be the conditional photon distribution in a nonempty shell. Write $`\sigma_k`$ for its complementary state. The classical entropy chain rule and concavity of quantum entropy imply

```math
\begin{aligned}
I_c(p,\mathcal N_\mu)
&=H(K)+\sum_k w_kH(p^{(k)})
  -S\!\left(\sum_k w_k\sigma_k\right)\\
&\le H(K)+\sum_k w_k I_c(p^{(k)},\mathcal N_\mu).
\end{aligned}
\tag{3.11}
```

All terms are well defined. Indeed, $`H(p)\le g(E)\lt\infty`$, and each shell has finite support. Moreover, the weighted shell entropies are bounded by

```math
\sum_k w_kH(p^{(k)})
\le\sum_k w_k\log_2(m2^k)
\le\log_2m+1.
```

The countable mixture form of concavity is therefore applicable without subtracting divergent quantities. It can also be obtained by finite grouping and passage to the limit using these entropy bounds.

By the shift observation and (3.5),

```math
I_c(p^{(k)},\mathcal N_\mu)
\le D_{m2^k}(\mu)+C.
\tag{3.12}
```

The angular partition into $`m2^k`$ bins exactly refines the partition into $`m`$ bins. Thus

```math
H_{m2^k}(\mu)\ge H_m(\mu),
\qquad
D_{m2^k}(\mu)\le D_m(\mu)+k.
\tag{3.13}
```

Inserting (3.12)–(3.13) into (3.11), and using (3.9)–(3.10), gives

```math
I_c(p,\mathcal N_\mu)
\le D_m(\mu)+C+H(K)+\mathbb E[K]
\le D_m(\mu)+C+3.
\tag{3.14}
```

Taking the supremum over every admissible $`p`$ proves the upper bound. The lower bound follows from (3.5) with $`d=m`$. Finally, $`0\le\log_2m-\log_2E\le1`$ for $`E\ge1`$, proving (3.3).

The proof controls the entire tail. It neither assumes that most of the probability is below a fixed cutoff nor replaces an average-energy constraint by a maximum-energy constraint.

## Information dimension and capacity growth

Define the lower and upper information dimensions of the phase law by

```math
\underline d_I(\mu)
=\liminf_{m\to\infty}\frac{H_m(\mu)}{\log_2m},
\qquad
\overline d_I(\mu)
=\limsup_{m\to\infty}\frac{H_m(\mu)}{\log_2m}.
\tag{3.15}
```

Dividing the bounded-error estimate by $`\log_2 E`$ yields

```math
\begin{aligned}
\liminf_{E\to\infty}\frac{Q_\mu(E)}{\log_2E}
&=1-\overline d_I(\mu),\\
\limsup_{E\to\infty}\frac{Q_\mu(E)}{\log_2E}
&=1-\underline d_I(\mu).
\end{aligned}
\tag{3.16}
```

If the information dimension $`d_I`$ exists, these limits agree. No exact-dimensionality, Fourier-decay assumption or existence of the dimension is needed for (3.2). A zero logarithmic slope does not imply zero capacity or even bounded capacity: the finite-resolution formula still distinguishes sublogarithmic growth from a finite ceiling.

Information dimension is an established classical notion. The spectral-entropy mechanism for a uniform time-averaged state already appears in [Guarneri's work](https://arxiv.org/abs/math-ph/9804009). The new operational conclusion here comes from the uniform cutoff comparison and the optimized mean-energy converse, rather than from assigning a dimension to the noise.

## Checks on the interpretation

For a deterministic phase, the channel is a known unitary, and its exact capacity is $`g(E)`$. Here $`H_m=0`$, so the theorem gives the correct logarithmic growth with bounded error. For uniform phase noise, the channel completely dephases the number basis and has zero quantum capacity; $`D_m=0`$ at every resolution. These are exact model checks, not numerical proofs of the general theorem.

The [bath and smoothing page](04-bath-and-smoothing.md) applies (3.2) to distributions with several physically distinct resolution regimes. The [interpretation](05-interpretation.md) separates the theorem's consequences from assumptions about losses, bath memory and practical code construction.
