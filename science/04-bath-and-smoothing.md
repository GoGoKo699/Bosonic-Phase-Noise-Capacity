# Finite spin baths and the effect of smooth phase noise

The capacity theorem gives a finite-resolution description of arbitrary phase noise. This chapter applies it to a geometric spin bath and proves that the prediction remains meaningful in the presence of independent continuous phase broadening. Both the bath-size crossover and the broadening crossover have errors bounded uniformly in the varying physical parameters.

The physical model is pure dephasing of one oscillator. Different channel uses receive independent bath states and independent broadening noise. The bath realization is inaccessible to the encoder and decoder. No photon loss, correlated reuse of one bath, or strong-converse statement is assumed.

## 1. Coordinates and the capacity estimate used here

It is convenient to describe a phase by $`X\in[0,1)`$, measured in cycles. The oscillator unitary is then $`e^{-2\pi iXN}`$. For a probability law $`\mu`$ of $`X`$, define

```math
J_m(X)=\lfloor mX\rfloor,
\qquad H_m(\mu)=H(J_m(X)),
\qquad D_m(\mu)=\log m-H_m(\mu).
\qquad\text{(B1)}
```

All logarithms are base two. The [capacity theorem](03-capacity.md) states that, for $`E\ge1`$ and $`m=\lceil E\rceil`$,

```math
D_m(\mu)-C
\le Q_\mu(E)
\le D_m(\mu)+C+3,
\qquad C=3.00379185809\ldots .
\qquad\text{(B2)}
```

The constant is independent of the phase law and energy. The lower bound is achieved as a coherent-information rate by a flat distribution on the first $`m`$ number states, followed by ordinary quantum coding across independent channel uses.

Let $`Z`$ be a standard real Gaussian, independent of $`X`$, and add the phase $`sZ\bmod1`$. Denote its circle law by $`G_s`$, so the total phase law is $`\mu*G_s`$. The width $`s`$ is in cycles; a Gaussian width $`\sigma`$ in radians corresponds to $`s=\sigma/(2\pi)`$. We use $`0<s\le1/10`$. Widths outside this small-noise range are not needed for the crossover statement.

## 2. Gaussian smoothing and finite-resolution entropy

### Theorem B1: quantized smoothing

For every Borel law of $`X\in[0,1)`$, every integer $`m\ge1`$, and $`0<s\le1/10`$,

```math
\boxed{
H_m(\mu*G_s)
=H_{\lceil\min\{m,1/s\}\rceil}(\mu)
 +\log^+(ms)+O(1),
}
\qquad\text{(B3)}
```

where $`\log^+t=\max\{0,\log t\}`$. The additive error is bounded by an absolute constant independent of $`m`$, $`s`$, and $`\mu`$. In particular, atoms and singular continuous measures are allowed.

Below the Gaussian resolution, the two quantized phase indices differ by a bounded-entropy integer error. Above it, Gaussian noise supplies $`\log(ms)+O(1)`$ bits inside each coarse phase cell. The proof makes both statements precise and keeps track of wrapping around the circle.

### 2.1 An integer error with bounded second moment has bounded entropy

For an integer-valued random variable $`W`$ with $`\mathbb EW^2\le v`$, define

```math
a(v)=\frac12\log\!\left[2\pi e\left(v+\frac1{12}\right)\right].
```

Then

```math
H(W)\le a(v).
\qquad\text{(B4)}
```

Indeed, add an independent uniform variable $`U`$ on $`[-1/2,1/2)`$. Its translated unit intervals have disjoint interiors, so $`h(W+U)=H(W)`$. Its variance is at most $`v+1/12`$. The Gaussian maximum-entropy inequality gives (B4). Finite second moment also guarantees that these entropies are finite; the same conclusion follows directly by comparison with a discrete Gaussian distribution.

We will only need the fixed constants $`a(4)`$ and $`a(20)`$.

### 2.2 Coarse angular bins: $`ms\le1`$

Put

```math
B=\lfloor mX\rfloor,\qquad R=mX-B\in[0,1),\qquad
Y=\lfloor m(X+sZ)\rfloor.
```

The unwrapped index satisfies

```math
Y=B+W,\qquad W=\lfloor R+msZ\rfloor.
\qquad\text{(B5)}
```

Since $`|W|\le|Z|+1`$, the bound $`\mathbb EW^2\le4`$ follows from $`(|Z|+1)^2\le2Z^2+2`$. Thus $`H(W)\le a(4)`$.

The wrapped phase index is $`J=Y\bmod m`$, with values in $`\{0,\ldots,m-1\}`$. Given $`B`$ and $`W`$, one determines $`J`$. Given $`J`$ and $`W`$, one determines $`B`$ uniquely in that same range. Independence of the error is unnecessary. Therefore

```math
H(J\mid B)\le H(W),\qquad H(B\mid J)\le H(W),
```

and hence

```math
|H_m(\mu*G_s)-H_m(\mu)|\le a(4).
\qquad\text{(B6)}
```

This proves (B3) in the first regime.

### 2.3 Fine angular bins: $`t=ms\ge1`$

Resolve the original phase at width $`s`$:

```math
A=\lfloor X/s\rfloor,\qquad R=X/s-A\in[0,1),
\qquad Y=\lfloor t(A+R+Z)\rfloor.
\qquad\text{(B7)}
```

First condition on $`A=a`$. Because $`Z`$ is independent of $`X`$, the continuous conditional variable

```math
V_a=t(a+R+Z)
```

has differential entropy at least $`\log t+h(Z)`$. This follows from concavity of differential entropy for a mixture of translated Gaussians. For unit-width quantization, $`h(V_a)\le H(\lfloor V_a\rfloor)`$: conditioning on its integer bin leaves a density supported on an interval of length one, whose differential entropy is at most zero. Consequently,

```math
H(Y\mid A=a)\ge\log t+h(Z).
\qquad\text{(B8)}
```

For the upper bound, use $`|Y-ta|\le t|R+Z|+1`$. Since $`0\le R<1`$, independence of $`Z`$ gives $`\mathbb E[(R+Z)^2\mid A=a]\le2`$. Thus

```math
\mathbb E[(Y-ta)^2\mid A=a]\le4t^2+2.
```

Adding independent uniform dither $`U`$ as in (B4) gives

```math
\mathrm{Var}(Y+U\mid A=a)
\le4t^2+2+\frac1{12}
\le\frac{73}{12}t^2.
```

Define

```math
b=\frac12\log\!\left(2\pi e\,\frac{73}{12}\right).
```

The Gaussian entropy bound then yields

```math
\log t+h(Z)
\le H(Y\mid A)
\le\log t+b.
\qquad\text{(B9)}
```

Next estimate the coarse label from the observed fine index by

```math
\widehat A(Y)=\lfloor Y/t\rfloor.
```

Writing $`u=t(A+R+Z)-Y\in[0,1)`$, the estimation error is

```math
A-\widehat A(Y)=-\lfloor R+Z-u/t\rfloor.
```

Its magnitude is at most $`|Z|+3`$, so its second moment is at most $`20`$. Equation (B4) and the fact that the error determines $`A`$ once $`Y`$ is known give

```math
H(A\mid Y)\le a(20).
\qquad\text{(B10)}
```

The identity

```math
H(Y)=H(A)+H(Y\mid A)-H(A\mid Y)
```

now implies

```math
H(A)+\log t+h(Z)-a(20)
\le H(Y)
\le H(A)+\log t+b.
\qquad\text{(B11)}
```

It remains to handle two changes of convention: circle wrapping, and the last possibly shorter cell in the width-$`s`$ partition.

Let

```math
L=\lfloor X+sZ\rfloor,\qquad
J=\lfloor m((X+sZ)\bmod1)\rfloor.
```

Then $`Y=mL+J`$, with $`0\le J<m`$. This is a bijection between $`Y`$ and $`(L,J)`$. Also $`|L|\le s|Z|+1\le|Z|+1`$, so $`H(L)\le a(4)`$. Hence

```math
H(Y)-a(4)\le H(J)\le H(Y).
\qquad\text{(B12)}
```

Finally set $`q=\lceil1/s\rceil`$. Each cell of the equal $`q`$-bin partition intersects at most two width-$`s`$ cells. Each width-$`s`$ cell intersects at most three equal $`q`$-bins, because $`qs\le1+s\le1.1`$. Bounded conditional support therefore gives

```math
H(A)\le H_q(\mu)+1,
\qquad
H_q(\mu)\le H(A)+\log3.
\qquad\text{(B13)}
```

Combining (B11)–(B13) proves the second regime of (B3). For example, one may use the explicit universal error bound

```math
C_G=\max\left\{
a(4),\ 1+b,\ \log3-h(Z)+a(20)+a(4)
\right\},
\qquad\text{(B14)}
```

where $`h(Z)=\tfrac12\log(2\pi e)`$. No optimization of this constant is needed. This completes the proof of Theorem B1. $`\square`$

## 3. The useful phase resolution and the capacity plateau

### Corollary B2: arbitrary phase law with Gaussian broadening

Let $`F=\min\{E,1/s\}`$. Uniformly in every Borel phase law, every $`E\ge1`$, and $`0<s\le1/10`$,

```math
\boxed{
Q_{\mu*G_s}(E)
=\log F-H_{\lceil F\rceil}(\mu)+O(1).
}
\qquad\text{(B15)}
```

**Proof.** First retain the exact integer cutoff $`m=\lceil E\rceil`$, and set $`T=\min\{m,1/s\}`$. Equations (B2) and (B3) give

```math
\begin{aligned}
Q_{\mu*G_s}(E)
&=\log m-H_{\lceil T\rceil}(\mu)-\log^+(ms)+O(1)\\
&=\log T-H_{\lceil T\rceil}(\mu)+O(1).
\end{aligned}
\qquad\text{(B16)}
```

The cancellation in the second line is exact. Now $`F\le T\le2F`$, so $`\log T-\log F`$ is bounded. The integers $`\lceil T\rceil`$ and $`\lceil F\rceil`$ also differ by at most a factor two. Their equal-bin partitions have bounded intersections in both directions, so their entropies differ by a universal constant. Replacing $`T`$ by $`F`$ proves (B15). $`\square`$

The corollary is an additive-accuracy statement; it does not assert an abrupt physical transition at exactly $`E=1/s`$. It says that increasing energy beyond inverse background width cannot change the capacity by an unbounded amount. The constants do not grow when the underlying law becomes singular or the broadening becomes weak.

### 3.1 Agreement with the unrestricted-energy smooth-law formula

For completeness, the same elementary argument gives the differential-entropy relation

```math
h((X+sZ)\bmod1)
=H_{\lceil1/s\rceil}(\mu)+\log s+O(1).
\qquad\text{(B17)}
```

To see this before wrapping, use $`X/s=A+R`$ from (B7). Conditional on $`A`$, the differential entropy of $`R+Z`$ lies between $`h(Z)`$ and $`\tfrac12\log(2\pi e\cdot5/4)`$, because $`\mathrm{Var}(R\mid A)\le1/4`$. Given $`A+R+Z`$, the estimator obtained by taking its floor has a bounded-entropy integer error. Thus

```math
h(A+R+Z)=H(A)+O(1).
```

Rescaling adds $`\log s`$. Wrapping loses only the conditional entropy of the winding index $`L`$, bounded in (B12), and (B13) replaces the width-$`s`$ partition by equal bins. This proves (B17).

The smoothed law has a bounded smooth density on the circle, so it satisfies the density regularity hypothesis used by Lami and Wilde [LW]. They identify its unrestricted-energy quantum capacity with relative entropy from the uniform phase density, which in these normalized coordinates is $`-h((X+sZ)\bmod1)`$. Equation (B17) therefore reproduces the plateau scale in (B15). This unrestricted-energy density-law formula is inherited; the finite-energy estimate follows directly from (B2) and Theorem B1.

## 4. A geometric spin bath

Fix $`r>2`$. Let $`B_1,B_2,\ldots`$ be independent fair Bernoulli variables, and let $`K`$ be a positive integer or infinity. Define

```math
X_K=(r-1)\sum_{k=1}^K B_kr^{-k},
\qquad \mu_K=\mathrm{law}(X_K\bmod1).
\qquad\text{(B18)}
```

The series converges absolutely. At $`r=3`$ and $`K=\infty`$, it gives the standard Cantor measure. The endpoints have zero probability for the infinite fair product law. For finite $`K`$, the support lies in $`[0,1-r^{-K}]`$, so it does not identify distinct atoms through the endpoint of the circle.

### Proposition B3: entropy resolved by the first bath spins

Let

```math
\delta=\frac1{\log_2r}.
```

Uniformly for all $`m\ge1`$ and all finite or infinite $`K`$,

```math
\boxed{
H_m(\mu_K)=\min\{K,\delta\log m\}+O_r(1).
}
\qquad\text{(B19)}
```

The error depends only on the fixed separation ratio $`r`$.

**Proof.** Put

```math
j=\min\{K,\lfloor\log_r m\rfloor\},
\qquad A_j=(B_1,\ldots,B_j).
```

For $`j=0`$, take $`A_j`$ to be a deterministic label. The entropy of this prefix is $`H(A_j)=j`$.

If $`j<K`$, a fixed prefix confines $`X_K`$ to an interval of length at most $`r^{-j}`$. Since $`mr^{-j}<r`$, this interval meets at most $`\lceil r\rceil+2`$ of the $`m`$ phase bins. Thus

```math
H(J_m(X_K)\mid A_j)\le\log(\lceil r\rceil+2).
\qquad\text{(B20)}
```

Different level-$`j`$ prefix intervals are separated by gaps of at least $`(r-2)r^{-j}`$. A phase bin has length $`1/m\le r^{-j}`$, so it meets at most $`\lceil1/(r-2)\rceil+2`$ of those intervals. Therefore

```math
H(A_j\mid J_m(X_K))
\le\log\!\left(\left\lceil\frac1{r-2}\right\rceil+2\right).
\qquad\text{(B21)}
```

If $`j=K<\infty`$, each prefix already determines a single atom. Distinct atoms are separated on the real interval by at least $`(r-1)r^{-K}`$, while $`m\ge r^K`$. Thus they lie in distinct phase bins, and $`H_m(\mu_K)=K`$ exactly in this range. The bounds above remain valid.

The identity

```math
H(J_m)-H(A_j)
=H(J_m\mid A_j)-H(A_j\mid J_m)
```

now gives $`H_m=j+O_r(1)`$. The difference between $`j`$ and $`\min\{K,\log_r m\}`$ is at most one, proving (B19). For example, a valid absolute error is

```math
c_r=1+\max\left\{
\log(\lceil r\rceil+2),
\log\!\left(\left\lceil\frac1{r-2}\right\rceil+2\right)
\right\}.
\qquad\text{(B22)}
```

No constant depends on $`K`$ or $`m`$. $`\square`$

## 5. Capacity crossover with finite bath size and broadening

For $`s=0`$, set $`F=E`$. For $`0<s\le1/10`$, set $`F=\min\{E,1/s\}`$. Equations (B2), (B15), and (B19) give

```math
\boxed{
Q_{\mu_K*G_s}(E)
=\log F-\min\{K,\delta\log F\}+O_r(1),
\qquad \delta=\frac1{\log_2r}.
}
\qquad\text{(B23)}
```

Here $`G_0`$ means no added broadening. The same error bound works for all bath sizes, all energies $`E\ge1`$, and all widths in the stated range. The result includes the infinite bath directly; it does not require an exchange of an infinite-bath limit with an infinite-energy limit.

The two forms of (B23) are

```math
Q(E)=
\begin{cases}
(1-\delta)\log F+O_r(1),&F\le r^K,\\
\log F-K+O_r(1),&F\ge r^K,
\end{cases}
\qquad\text{(B24)}
```

with only the first branch for $`K=\infty`$. They identify three possible energy ranges.

| Range | Capacity to bounded additive error | Physical information resolved |
|---|---|---|
| $`1\ll E\ll\min\{r^K,1/s\}`$ | $`(1-\delta)\log E`$ | A number of bath spins growing with $`\log E`$ |
| $`r^K\ll E\ll1/s`$, when this range exists | $`\log E-K`$ | All $`K`$ bath spins |
| $`E\gg1/s`$, for $`s>0`$ | $`\log(1/s)-\min\{K,\delta\log(1/s)\}`$ | Resolution limited by continuous broadening |

For a finite bath without broadening, the asymptotic coefficient of $`\log E`$ is one. For an infinite bath without broadening, it is $`1-\delta`$. At every fixed positive broadening width it is zero, because the capacity is bounded as $`E`$ grows. The finite-energy crossover shows precisely where the fractional coefficient can be observed before finite bath size or continuous noise changes the behavior. Bounded log-periodic variations are compatible with these statements; a pointwise derivative with respect to $`\log E`$ is not asserted.

Only $`K`$ of order $`\log_r E`$ is needed for the fractional regime over a prescribed finite energy range. The infinite singular measure is therefore a useful limit of a finite resource family, rather than the sole setting in which the prediction applies.

## 6. Hamiltonian realization and independence of channel uses

For a bath of $`K`$ spins, let $`P_k`$ be the projector onto one of the two states of spin $`k`$, and prepare the product state $`(I_2/2)^{\otimes K}`$. During an interaction of duration $`t_0>0`$, choose

```math
H_{\mathrm{int}}=N\otimes\mathcal B_K,
\qquad
\mathcal B_K=\frac{2\pi(r-1)}{t_0}
\sum_{k=1}^K r^{-k}P_k.
\qquad\text{(B25)}
```

Tracing out the bath after this interaction gives exactly the phase law in (B18). The bath eigenvalue selected by the product state is the sum of independent Bernoulli contributions. A diagonal bath Hamiltonian commutes with the coupling and leaves the initial bath state stationary, so it does not alter this reduced channel.

The bath coupling is uniformly bounded:

```math
0\le\mathcal B_K\le\frac{2\pi}{t_0}I,
\qquad\text{(B26)}
```

including in the infinite-spin limit. Thus the geometric example does not require a divergent total coupling strength. With the projector convention in (B25), the coupling is nonnegative. An oscillator free Hamiltonian $`\omega N`$, $`\omega\ge0`$, and a nonnegative diagonal bath Hamiltonian give a semibounded total Hamiltonian. In a centered Pauli convention, one may instead choose $`\omega>\|\mathcal B_K\|`$ to ensure semiboundedness. The two conventions differ by a known oscillator rotation and give the same capacity.

For infinitely many spins, the product state is understood as a state on the spin algebra, and the absolutely summable coupling defines a bounded bath observable. One need not posit a trace-class maximally mixed state on an infinite tensor product. The finite-$`K`$ realizations already establish every finite bath-size crossover. If an infinite bath Hamiltonian is desired with finite total energy, summable nonnegative spin gaps are one admissible choice; no thermodynamic preparation cost is included in the oscillator's mean-photon budget.

Independence is a separate assumption from stationarity. Each use of the memoryless channel must receive a fresh independent product bath, or a bath reset independently to that state. Reusing one unchanged bath would correlate the phases across uses and would define a different communication channel. Likewise, the optional Gaussian phase is sampled independently for each use and independently of the spin bath. The interaction conserves photon number, so this chapter concerns pure dephasing throughout.

The geometric bath spectrum is not a new construction. Ben Attar and Bar-Gill [BAG] identify the Cantor spectral measure for exponentially decaying Ising spin couplings and use it to study non-Gaussian Ramsey dephasing. Their central system is a qubit. Here the same type of bounded bath observable couples to oscillator number, and the operational quantity is optimized quantum communication under a photon constraint.

## Sources

**[LW]** L. Lami and M. M. Wilde, *Exact solution for the quantum and private capacities of bosonic dephasing channels*, Nature Photonics **17**, 525–530 (2023). [Primary manuscript, arXiv:2205.05736v2](https://arxiv.org/html/2205.05736v2); [journal article](https://doi.org/10.1038/s41566-023-01190-4). For the bounded smooth densities produced by Gaussian broadening, their unrestricted-energy capacity formula is the relative entropy from the uniform density. It supplies the exact interpretation of the smooth-law plateau.

**[BAG]** K. I. O. Ben Attar and N. Bar-Gill, *Dephasing in the central spin problem with long-range Ising spin-bath coupling*, [primary manuscript, arXiv:2409.12749v1](https://arxiv.org/html/2409.12749v1), Section IV and Proposition 2. The paper provides the geometric spin-bath spectral example and its Cantor measure. The oscillator-number coupling and optimized capacity consequence are distinguished above.

The quantization and smoothing estimates in this chapter are proved explicitly. The channel-capacity input is the [main theorem](03-capacity.md), whose coding-theorem assumptions and attribution are stated there.
