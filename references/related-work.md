# Related work and contribution boundaries

This account compares the finite-energy result with the primary literature checked on 3 November 2026. Bibliographic keys refer to [sources.bib](sources.bib). The comparisons identify the assumptions and conclusions of the cited results; they do not assert exhaustive priority.

## Result being compared

For a Borel probability measure $`\mu`$ on the phase circle, consider independent uses of

```math
\mathcal N_\mu(\rho)=\int e^{-i\theta N}\rho e^{i\theta N}\,\mu(d\theta),
\qquad N=\sum_{n\ge0}n|n\rangle\langle n|.
```

The realized phase is inaccessible. The resource constraint is mean input photon number at most $`E`$, averaged across uses. Define the entropy of the equal-width phase histogram and its deficit by

```math
H_m(\mu)=H\!\left(\left\lfloor\frac{m\Theta}{2\pi}\right\rfloor\right),
\qquad D_m(\mu)=\log_2m-H_m(\mu),\qquad\Theta\sim\mu.
```

The central statement is the uniform, optimized, finite-energy bound

```math
D_m(\mu)-C\le I_c(u_m,\mathcal N_\mu)
\le Q_\mu(E)\le D_m(\mu)+C+3,
\qquad m=\lceil E\rceil,\quad E\ge1,
```

where $`u_m`$ is uniform on the first $`m`$ Fock levels and

```math
C=\frac\pi2\alpha<3.004,\qquad
\alpha=2\max_{0<x<1}\sqrt{x(1-x)}
\left|\log_2\frac{x}{1-x}\right|.
```

Thus the additive error is independent of the noise measure and the energy. The statement covers atomic and singular continuous laws and does not require an information-dimension limit. Its main content is the evaluation of an existing coherent-information optimization to constant accuracy, together with a converse that controls arbitrary photon-number tails. No optimality of the displayed constant is asserted.

## Capacity theory inherited from earlier work

### Generalized dephasing and energy-constrained coding

The dilation $`|n\rangle\mapsto|n\rangle|e_n\rangle`$, with $`e_n(\theta)=e^{-in\theta}`$, has complement $`\rho\mapsto\sum_n\rho_{nn}|e_n\rangle\langle e_n|`$. Measuring photon number and preparing $`|e_n\rangle`$ is a degrading map. The corresponding diagonal-input reduction is a standard generalized-dephasing argument; see Section 2, equations (4)--(9), of [D'Arrigo, Benenti and Falci](https://arxiv.org/pdf/quant-ph/0703014v3) (`DArrigoBenentiFalci2007`). Their memory-channel applications have a different operational model from the independent uses considered here.

[Wilde and Qi](https://arxiv.org/pdf/1609.01997v2), Theorem 3, equation (204), establish the energy-constrained single-letter coding theorem for degradable channels under the Gibbs-observable and finite-output-entropy conditions (`WildeQi2018`). Here these conditions follow from the photon-number Gibbs partition function and the entropy bound $`H(p)\le g(E)`$. Consequently,

```math
Q_\mu(E)=\sup_{\sum_nnp_n\le E}
\left[H(p)-S\!\left(\sum_np_n|e_n\rangle\langle e_n|\right)\right]
```

is an inherited coding-theorem application. The validity of this reduction for a Borel measure follows directly from the $`L^2(\mu)`$ dilation; it is not the proposed main contribution.

### Exact unconstrained capacity for phase densities

[Lami and Wilde](https://doi.org/10.1038/s41566-023-01190-4) determine the unassisted and two-way assisted quantum and private capacities without an energy constraint (`LamiWilde2023`). Their [Supplementary Theorem S7](https://arxiv.org/html/2205.05736v2) gives $`D(p\|u)=\log_2(2\pi)-h(p)`$ under the stated density regularity condition $`p\in L^{\alpha_0}`$ for some $`\alpha_0>1`$. Their construction uses uniform Fock distributions and Toeplitz spectral asymptotics. These are direct antecedents of the present flat-input lower bound and smooth-noise saturation interpretation. The theorem as stated there is not an arbitrary-Borel-measure, finite-energy estimate with an error uniform over the noise law.

### Exact finite-energy variational characterization

[Arqand and Smith](https://arxiv.org/abs/2610.13854), version 1, define their phase channel using a probability density in Definition 2.8 (`ArqandSmith2026`). Theorems 3.3 and 3.5 identify four finite-energy assisted and unassisted capacities with the same Fock-diagonal coherent-information optimization. Their constraint allows adaptive inputs with unconditional energy averaged across uses. Section 4 leaves the optimizing or near-optimal photon distributions as a further problem. This work therefore supplies the closest finite-energy characterization, not the histogram evaluation above. The present core theorem concerns ordinary unassisted quantum capacity; it does not claim a new assistance equality for singular measures.

## Entropy and Toeplitz results: what transfers and what remains

### The product-Hamiltonian entropy-rate bound is established

[Childs, Leung and Vidal](https://arxiv.org/pdf/quant-ph/0303097), Section IV, Theorem 6 and Corollary 7, give the product-Hamiltonian entangling capacity $`\alpha\Delta_A\Delta_B/4`$ (`ChildsLeungVidal2004`). This implies the dimension-independent inequality

```math
\left|\frac{d}{dt}S(\rho_A(t))\right|
\le\alpha\|A\|\|B\|
```

for evolution generated by $`A\otimes B`$. The scalar inequality and row-sum proof used in this project are a direct form of that established bound.

The application here rounds each phase to its bin midpoint. On the first $`d`$ Fock levels, the number generator can be centered to norm $`(d-1)/2`$, while the residual phase has norm at most $`\pi/d`$. Their product is bounded independently of $`d`$. This yields an entropy comparison for **every** input distribution within the cutoff. The relevant addition is this application and its operational consequence, not a new entangling-rate theorem.

### Spectral dimensions already control uniform-orbit entropy slopes

[Guarneri](https://numdam.org/item/AIHPA_1998__68_4_491_0/), Theorem 1, proves $`S(\psi,T)\sim D\ln T`$ for exactly scaling spectral measures (`Guarneri1998`). Propositions 3--5 give broader dimension bounds. The remark following the proof identifies the nonzero spectrum with a normalized $`T\times T`$ Toeplitz autocorrelation matrix. It is therefore the same spectral-entropy mechanism that appears for a uniform Fock input here. The existence of a fractional entropy slope for regular fractal phase laws is inherited. A slope for that prescribed input does not establish an optimized converse under a mean photon-number constraint, nor a universal additive bound for irregular measures.

### General test-function theorems do not supply the stated uniform bound

The relevant Szegő and Avram--Parter results concern limits of normalized traces of test functions of Toeplitz matrices. Lami--Wilde's Lemma S6 uses Serra-Capizzano's growth-condition theorem (`SerraCapizzano2002`). A broader directly inspected primary formulation is [Böttcher, Grudsky and Maksimenko](https://www.numdam.org/item/10.1016/j.crma.2008.06.002.pdf), Theorems 2 and 5 (`BottcherGrudskyMaksimenko2008`). Its symbol is an $`L^1`$ function; convex domination controls admissible unbounded test functions. The associated [longer primary preprint](https://www.tu-chemnitz.de/mathematik/preprint/2007/PREPRINT_24.pdf), especially Theorem 8.2, makes these hypotheses explicit.

These are powerful density-symbol asymptotics. Their stated conclusions do not provide a noise-uniform finite-size comparison with the entropy of a phase histogram, and they do not optimize nonuniform photon distributions. A generic weak spectral-distribution limit is insufficient: for a point phase law, the Toeplitz matrix has eigenvalues $`d,0,\ldots,0`$. Its empirical eigenvalue distribution tends to a point mass at zero, while $`d^{-1}\mathrm{Tr}(T_d\log T_d)=\log d`$. The entropy contribution from the large eigenvalue must be retained.

For the flat input, the present estimate reads

```math
\left|S(T_d(\mu)/d)-H_d(\mu)\right|\le C.
```

Even this fixed-input statement is not by itself the whole capacity result. The proof uses the stronger input-uniform rounded-channel comparison and then removes the hard cutoff. A dyadic shell label $`K=\lfloor\log_2(1+n/m)\rfloor`$ has $`H(K)\le2`$ and $`\mathbb EK\le1`$ under the mean-energy budget. Exact refinement of the phase partitions then bounds the entire tail contribution by three additional bits.

None of the primary results reviewed above supplies the complete uniform optimized law. An existing input-uniform entropy comparison or an equivalent mean-energy capacity theorem would be a material antecedent. The contribution should therefore be described by the proved statement and its assumptions, without a claim that all possible mathematical formulations have been excluded.

## Information dimension and physical phase laws

[Wu and Verdú](https://doi.org/10.1109/TIT.2010.2050803), Section III, give the quantized-entropy definition of lower and upper Rényi information dimension and its classical compression interpretation (`WuVerdu2010`). The definition is inherited. Substituting it into the finite-energy bound gives the quantum-capacity conclusions

```math
\liminf_{E\to\infty}\frac{Q_\mu(E)}{\log E}=1-\overline d_I(\mu),
\qquad
\limsup_{E\to\infty}\frac{Q_\mu(E)}{\log E}=1-\underline d_I(\mu).
```

These are consequences of the optimized bound, rather than a new definition of dimension or a new classical quantization theorem. The finite-resolution statement remains meaningful when the dimension limit does not exist.

[Ben Attar and Bar-Gill](https://arxiv.org/html/2409.12749v1), Section IV, Proposition 2, identify a Cantor spectral measure for geometrically decreasing Ising-bath couplings (`BenAttarBarGill2024`). Their central system is a qubit and their observable is Ramsey dephasing. The geometric bath and its non-Gaussian behavior are therefore prior ingredients. The model application here couples the same kind of bounded bath observable to oscillator number and evaluates its communication capacity, including finite-bath resolution and independent Gaussian broadening. Each independent channel use requires a fresh or independently reset bath. Repeated interaction with one static bath is a different, correlated channel model.

In particular, a finite bath eventually has atomic-law scaling, and fixed smooth broadening eventually limits the useful phase resolution. The corresponding fractional-slope window, finite-bath crossover, and saturation are finite-energy consequences of the main result. They should not be presented as robustness of an infinite-energy fractal slope to arbitrary smoothing.

## Numerical scope and remaining boundaries

Numerical Toeplitz spectra test flat-input coherent information and parameter conventions. They do not numerically optimize capacity or prove the mean-energy converse. [Audenaert's sharp entropy-continuity inequality](https://doi.org/10.1088/1751-8113/40/28/S18) (`Audenaert2007`) is used only to bound entropy error from a finite approximation to an infinite bath. It is separate from the dimension-independent phase-rounding argument.

The result does not establish a new bosonic code construction, an optimal additive constant, a strong converse under a mean-only constraint, or an assisted-capacity equality for arbitrary singular laws. Photon loss, bath reuse, and uncertainty in the noise parameters are outside the stated channel model.

## Source and version notes

The compared mathematical statements were read in the primary manuscripts or published texts linked above. Arqand--Smith was checked against the complete arXiv-labelled version-1 PDF, including its density assumption, capacity theorems, and conclusion. Serra-Capizzano's bibliographic details were cross-checked against the author's institutional record and the primary references above; the precise formulation used here is the one reproduced as Lami--Wilde Lemma S6, supplemented by the directly inspected Böttcher--Grudsky--Maksimenko theorem. Bibliography dates use publication records or arXiv submission histories, not an automatically rendered internal date.
