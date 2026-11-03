# From Wilde's quantum Shannon theory to phase-noise capacity

[Learning route](README.md) · [Milestone map](milestones.md) · [Scientific account](../science/README.md)

A random phase rotation leaves an oscillator's photon-number probabilities unchanged while changing the coherence between different number states. Quantum communication depends on that coherence. This project asks how much quantum information survives when the sender's mean photon number is bounded and the phase distribution can have arbitrary fine structure.

Wilde's book supplies the language of states, channels, entropy, and quantum capacity. The bridge below explains how that language leads to the particular optimization studied here, and which additional results evaluate it to a universal additive error. Each reading supports a specific part of the argument; reading the whole book is unnecessary for following the project.

## Selected source

**Mark M. Wilde, _Quantum Information Theory_, second edition, Cambridge University Press, 2017.** [Publisher page](https://www.cambridge.org/core/books/quantum-information-theory/247A740E156416531AA8CB97DFDAE438) · [DOI](https://doi.org/10.1017/9781316809976) · [Publisher contents](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf).

The section titles and starting pages below refer to the **published 2017 second edition**. Wilde also provides an [author-hosted reading draft](https://www.markwilde.com/qit-notes.pdf), dated December 5, 2021 in the linked copy. Its pagination differs. The section-level pointers below are suitable for navigating both, but the listed pages belong to the published edition. No finer draft-only subsection or theorem numbering is needed here.

## Reading routes

### States and reductions

Read **§4.1, Noisy Quantum States** (p. 102), and **§4.3, Composite Noisy Quantum Systems** (p. 117), in Chapter 4, _The Noisy Quantum Theory_.

The essential distinction is between the state of a combined system and the state available to one observer. A density operator describes a possibly mixed state; a partial trace gives the state of one subsystem. In this project, receiver and environment states come from two different partial traces of the same channel isometry. For a cutoff-supported input, the environment entropy can be computed from the finite-dimensional auxiliary marginal of a purification, even when the environment Hilbert space is infinite dimensional.

### Channels and environments

Continue with **§4.4, Quantum Evolutions** (p. 129), and **§4.5, Interpretations of Quantum Channels** (p. 141). Then read **§5.1, Purification** (p. 165), and **§5.2, Isometric Evolution** (p. 168), in Chapter 5, _The Purified Quantum Theory_.

A channel describes the receiver's output; an isometric extension retains the environment as well. Tracing out the receiver defines a complementary channel. The generalized-dephasing construction in this route is the starting point for the oscillator channel: photon number is preserved at the receiver, while the environment acquires a photon-number-dependent state. The [arbitrary-measure dilation below](#a-dilation-for-every-borel-phase-law) makes this construction work even when the phase law has no density.

### Entropy and conditional information

In Chapter 10, _Classical Information and Entropy_, use **§10.1, Entropy of a Random Variable** (p. 268), **§10.2, Conditional Entropy** (p. 273), **§10.5, Relative Entropy** (p. 276), and **§10.7, Entropy Inequalities** (p. 279).

In Chapter 11, _Quantum Information and Entropy_, use **§11.1, Quantum Entropy** (p. 301), **§11.2, Joint Quantum Entropy** (p. 306), **§11.4, Conditional Quantum Entropy** (p. 311), **§11.8, Quantum Relative Entropy** (p. 321), and **§11.9, Quantum Entropy Inequalities** (p. 327).

Classical entropy measures uncertainty in a phase-bin label or a photon-number distribution. Quantum entropy measures the spectrum of a density operator. Both enter the capacity formula, but they describe different objects. Conditional entropy, concavity, and data processing explain which operations can increase or decrease the relevant information. The classical chain rule later allows the photon distribution to be resolved into energy shells without losing the contribution of its tail.

### Coherent information and degradability

Read **§11.5, Coherent Information** (p. 313), in Chapter 11, _Quantum Information and Entropy_. Continue with **§13.5, Coherent Information of a Quantum Channel** (p. 393), in Chapter 13, _The Information of Quantum Channels_. Use **§5.2** for the complementary-channel construction and degradability examples.

For a fixed input, coherent information is the receiver entropy minus the complementary-output entropy. Degradability means that a channel acting on the receiver's output can reproduce the environment's output. This property gives concavity in the input and additivity of the optimized channel quantity. Here it supports the operational capacity reduction and, for the rounded finite channel, proves that averaging over a symmetry group cannot hurt coherent information. “Degradability” names the concept in this route; the verified section titles are those given above.

### Operational quantum capacity

In Chapter 24, _Quantum Communication_, read **§24.1, The Information-Processing Task** (p. 643), **§24.3, The Quantum Capacity Theorem** (p. 646), **§24.4, The Direct Coding Theorem** (p. 647), and **§24.5, Converse Theorem** (p. 654).

These sections connect an entropy expression to an operational task: transmitting half of an entangled state with error tending to zero over increasingly long blocks. Achievability supplies codes below a rate; a converse constrains all allowed codes. The project's lower bound uses coherent-information coding, while its upper bound must control every allowed photon distribution. The energy-constrained, infinite-dimensional step uses the primary theorem identified [below](#energy-constrained-operational-coding).

For supporting detail within the same anchor, **§9.1, Trace Distance** (p. 230), and **§9.2, Fidelity** (p. 243), explain error measures; **§15.1, The Typical Subspace** (p. 444), explains a coding mechanism. **§11.10, Continuity of Quantum Entropy** (p. 339), is relevant to finite-dimensional numerical error estimates. The dimension-independent phase-rounding estimate instead uses the product-interaction argument below.

## Notation and assumptions

All logarithms in the project are base two. Classical entropy and relative entropy are in bits; the resulting quantum communication rate is in qubits per channel use.

| Object | Translation into this project |
|---|---|
| Quantum entropy | Wilde commonly writes the entropy of system A as $`H(A)`$. Here $`S`$ denotes von Neumann entropy, while $`H`$ denotes classical Shannon entropy. |
| Input and outputs | The oscillator is the input and receiver system. When discussing the dilation here, $`F`$ labels the environment, so $`E`$ can consistently denote the photon budget. |
| Channel and generator | The channel $`\mathcal N_\mu`$ and the photon-number operator $`N`$ are different objects. The latter generates phase rotations. |
| Coherent information | The quantity for a fixed input is written $`I_c`$. In Wilde §13.5, the optimized channel quantity is denoted $`Q(\mathcal N)`$; the operational capacity can require regularization. Here $`Q_\mu(E)`$ always denotes the operational capacity with a mean-photon constraint. |
| Uniform distributions | The same numerical vector can represent uniform probabilities on phase bins or on Fock levels. The surrounding system determines which meaning applies. The capacity lower bound uses a uniform Fock input. |
| Photon resource | $`E`$ bounds a mean photon number. A cutoff dimension $`d`$ restricts support to $`d`$ number states and is a different constraint. |

For a channel input with purification on a reference system R, the state and channel forms of coherent information agree:

```math
I(R\rangle B)_\omega
=S(\omega_B)-S(\omega_{RB})
=S(\mathcal N_\mu(\rho))
 -S(\mathcal N_\mu^c(\rho)).
```

The last equality uses purity of the reference–receiver–environment state after the isometry. The reference keeps track of the quantum information that should remain entangled with the receiver; it is not an additional communication resource.

The full model uses independent applications of one known phase law. The realized phase is not supplied to either party. The code's encoded maximally mixed logical state satisfies the mean input-energy constraint averaged across uses. The capacity is unassisted, and the channel includes phase noise only. These assumptions are specified in the [model and coding problem](../science/01-model.md#the-charged-resource); the textbook's finite-dimensional discussion does not impose them automatically on an oscillator.

## The missing bridges

### A dilation for every Borel phase law

The noise law $`\mu`$ is a probability measure on the circle. It can describe discrete phases, a density, a singular continuous distribution, or mixtures. Writing the channel as an integral against $`\mu(d\theta)`$ therefore matters: a probability density need not exist.

Take the environment to be $`F=L^2(\mu)`$, the Hilbert space of square-integrable functions with respect to that measure. Define

```math
e_n(\theta)=e^{-in\theta},
\qquad
V|n\rangle=|n\rangle\otimes|e_n\rangle.
```

Each environment vector has unit norm. Orthogonality of the oscillator number states makes $`V`$ an isometry even when the environment vectors overlap. Its complementary channel is

```math
\mathcal N_\mu^c(\rho)
=\sum_{n\ge0}\rho_{nn}|e_n\rangle\langle e_n|.
```

The receiver retains the same number probabilities. Measuring that number and preparing the corresponding environment state therefore reproduces the complement, proving degradability. Also, replacing the input by its number-diagonal part preserves the complement and cannot reduce receiver entropy. Thus optimization may be restricted to photon distributions. This is the generalized-dephasing mechanism from the anchor, implemented for arbitrary measures in [the model](../science/01-model.md#an-arbitrary-measure-dilation).

### Energy-constrained operational coding

For a photon distribution $`p=(p_n)_{n\ge0}`$, define the complementary state

```math
\sigma_p=\sum_{n\ge0}p_n|e_n\rangle\langle e_n|.
```

The relevant primary result is **Wilde–Qi, Theorem 3**, with the average-energy coding convention in their Section III and equivalence result in Theorem 1: [primary paper](https://arxiv.org/pdf/1609.01997v2), bibliographic key `WildeQi2018`. Applied here, it gives

```math
Q_\mu(E)
=\sup_{\substack{p_n\ge0,\ \sum_n p_n=1\\
                  \sum_n n p_n\le E}}
\left[H(p)-S(\sigma_p)\right].
```

The infinite-dimensional hypotheses require a check. The number operator is a Gibbs observable because its thermal partition function is finite for every positive inverse-temperature parameter. The maximal entropy at fixed mean photon number is finite:

```math
\mathrm{Tr}e^{-\beta N}=(1-e^{-\beta})^{-1},
\qquad \beta\gt0,
\qquad
H(p)\le g(E),
```

```math
g(E)=(E+1)\log_2(E+1)-E\log_2 E.
```

Both receiver and complementary-output entropies are at most $`H(p)`$. Along with degradability, these bounds verify the applicable coding theorem's conditions and ensure that the coherent-information difference is finite. The complete reduction is in [the model](../science/01-model.md#why-the-single-letter-formula-is-valid-here). This imported operational theorem identifies the optimization; the subsequent project arguments estimate its value.

### Entropy change under a product interaction

The second imported ingredient is **Childs–Leung–Vidal's product-Hamiltonian entanglement bound**, Section IV, Theorem 6 and Corollary 7: [primary paper](https://arxiv.org/pdf/quant-ph/0303097), bibliographic key `ChildsLeungVidal2004`.

If a pure bipartite state with at least one finite-dimensional system evolves under a bounded product Hamiltonian $`A\otimes B`$, the relevant consequence is

```math
|S(\rho_A(t))-S(\rho_A(0))|
\le |t|\alpha\|A\|\,\|B\|,
```

```math
\alpha
=2\max_{0\lt x\lt1}\sqrt{x(1-x)}
\left|\log_2\frac{x}{1-x}\right|
=1.91227328893\ldots .
```

The bound depends on the interaction strengths, without a factor growing with Hilbert-space dimension. Centering either operator by subtracting a scalar multiple of the identity removes only local unitary evolution and can reduce the norm. [Lemma P2](../science/02-phase-quantization.md#lemma-p2-entropy-rate) gives the bound and its application when one system is finite dimensional and the other may be infinite dimensional. This established entropy-rate result is the tool used for the phase comparison.

### Phase quantization uniformly over inputs

Restrict photon number temporarily to $`0,\ldots,d-1`$. Partition the phase circle into $`d`$ equal half-open bins, so an atom on a boundary has an unambiguous assignment. If $`q_j`$ is the probability of bin $`j`$, write

```math
H_d(\mu)=H(q),
\qquad
D_d(\mu)=\log_2 d-H_d(\mu).
```

Round the phases in each bin to its midpoint, producing a discrete law $`\nu_d`$. The original and rounded complementary states admit purifications on the same space. A product interaction connects those purifications: its number factor can be centered to norm $`(d-1)/2`$, while its residual-phase factor has norm at most $`\pi/d`$. The two factors compensate as the cutoff grows. The imported entropy bound therefore gives, for **every** photon distribution supported in the cutoff,

```math
|I_c(p,\mathcal N_\mu)-I_c(p,\mathcal N_{\nu_d})|
\le C_d,
\qquad
C_d=\frac{\pi\alpha}{2}\left(1-\frac1d\right).
```

The finite marginal of this auxiliary purification is a Gram matrix with the complementary state's nonzero spectrum. It must be distinguished from the physical receiver output, which remains the diagonal input state.

The rounded channel is cyclic dephasing. Its symmetry and coherent-information concavity make the uniform input optimal, with exact value $`D_d(\mu)`$. Combining this fact with the input-uniform comparison bounds the original cutoff optimum and supplies a flat-input lower bound. The universality over inputs is what permits optimization; an estimate only for a preselected flat input would supply no converse. The full construction and proof are [Theorem P1 and its proof](../science/02-phase-quantization.md#theorem-p1-cutoff-capacity-and-a-flat-input).

### Dyadic shells under a mean constraint

A mean photon budget allows arbitrarily high photon numbers with small probability. The cutoff result therefore needs an additional argument before it can bound the stated capacity. Set $`m=\lceil E\rceil`$ for $`E\ge1`$, and attach the shell label

```math
K(n)=\left\lfloor\log_2\!\left(1+\frac nm\right)\right\rfloor.
```

Shell $`k`$ contains $`m2^k`$ consecutive number states. Under any admissible photon distribution,

```math
\mathbb E[2^K]\le2,
\qquad
\mathbb E[K]\le1,
\qquad
H(K)\le2.
```

The first bound follows from the mean energy; the second uses concavity of the logarithm; the third uses the maximum entropy of a nonnegative integer with mean at most one. These are classical information tools applied to a particular partition of the photon states.

Shifting a shell down to start at zero only applies one common unitary to its environment states, so its coherent information obeys the cutoff bound for that shell's size. Meanwhile, the phase partition with $`m2^k`$ bins refines the one with $`m`$ bins, yielding

```math
D_{m2^k}(\mu)\le D_m(\mu)+k.
```

The entropy chain rule for the shell label and concavity of the complementary entropy now bound every admissible input:

```math
I_c(p,\mathcal N_\mu)
\le D_m(\mu)+C+H(K)+\mathbb E[K]
\le D_m(\mu)+C+3,
\qquad C=\frac{\pi\alpha}{2}.
```

This retains the entire tail. The shell decomposition and the justification for countable entropy mixtures appear in [the capacity proof](../science/03-capacity.md#dyadic-shells-control-the-whole-energy-tail).

## Assemble the capacity estimate

The uniform distribution $`u_m`$ on the first $`m`$ Fock levels has mean photon number $`(m-1)/2\le E`$. It supplies a feasible lower bound through the cutoff comparison. The shell argument supplies the upper bound over all inputs. Thus [Theorem 1](../science/03-capacity.md#main-theorem) states

```math
D_m(\mu)-C
\le I_c(u_m,\mathcal N_\mu)
\le Q_\mu(E)
\le D_m(\mu)+C+3,
\qquad m=\lceil E\rceil,
\qquad C=3.00379185809\ldots .
```

The error is independent of the phase law and energy. The result evaluates the optimized, mean-energy-constrained quantum capacity to a fixed additive accuracy; it does not identify an exact optimizer or optimal error constant. Its physical content is that communication is governed by the entropy deficit of the noise at the angular resolution supplied by the photon budget.

The [milestone map](milestones.md) connects these ingredients into the project's full story. The [capacity page](../science/03-capacity.md#information-dimension-and-capacity-growth) derives the growth law from information dimension, and the [bath and smoothing page](../science/04-bath-and-smoothing.md) explains the physical examples and their resolution regimes. The [related-work account](../references/related-work.md) and [research bibliography](../references/sources.bib) preserve the distinction between textbook foundations, imported primary theorems, and the project's comparison and converse arguments.
