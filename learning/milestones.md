# Thirty milestones for the capacity argument

This map follows the scientific question: how does the mean photon number determine quantum communication through an oscillator with an arbitrary phase-noise law? Its targets connect the mathematical objects, the optimized capacity theorem, and the finite-bath and smoothing consequences into one account.

The allocation is **14 milestones in background/preliminaries** and **16 in narrative/innovation**. The background phase must connect quantum states and channels, classical and quantum entropy, communication rates, and an infinite-dimensional energy budget. It ends with the complete optimization problem. The narrative phase has slightly more space because the input-uniform phase comparison and the mean-energy converse are separate steps, and their physical meaning requires the bath and smoothing results. Within each phase the order runs from individual objects and mechanisms to an integrated conclusion.

The sole educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)**. The [anchor and source bridge](anchor.md) identifies the verified edition and explains how its notation connects to this project. Textbook section numbers below refer to that edition. Primary research papers are cited for their proof ingredients and attribution; they do not add educational anchors. The project pages supply the oscillator specialization, energy-constraint checks, and derivations beyond the textbook.

Each milestone has a central question, an understanding target, its earlier dependencies and role in the story, a conceptual connection, and precise source pointers. The targets cover the argument as a whole without attempting to reproduce every technical lemma or every neighboring subject. The phase assigned by each section applies to all milestones within it.

## Phase I — Background and preliminaries: M01–M14

### M01 — The oscillator as an information carrier

**Central question.** What information can a state of one oscillator carry beyond its photon-number probabilities?

**Understanding target.** Distinguish number states, superpositions, and mixtures in the number basis. Identify the diagonal entries of a density operator as number probabilities and its off-diagonal entries as coherences. Relate the number operator $`N`$ to the mean photon number charged by the model.

**Dependencies and story role.** Entry point. It introduces the physical carrier and the state information that phase noise will affect.

**Conceptual connection.** The textbook description of a quantum state becomes a concrete oscillator model in which coherence and energy have different roles.

**Source pointers.** [Wilde](anchor.md#states-and-reductions), §4.1, “Noisy Quantum States”; [model](../science/01-model.md), “Channel and phase convention” and “The charged resource,” equations (1.1)–(1.4).

### M02 — A phase rotation and a random phase law

**Central question.** How does uncertainty in a phase change an oscillator state while preserving its photon-number distribution?

**Understanding target.** Explain the deterministic action of $`e^{-i\theta N}`$ and why averaging it multiplies a coherence between $`n`$ and $`k`$ by $`\widehat\mu(n-k)`$. Distinguish the known noise law from the hidden realized phase, and independent channel uses from repeated interaction with one static environment.

**Dependencies and story role.** Uses M01. It turns the physical carrier into the specific noisy communication channel.

**Conceptual connection.** Random unitary evolution connects classical uncertainty about a phase to selective loss of quantum coherence.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§4.4–4.5, “Quantum Evolutions” and “Interpretations of Quantum Channels”; [model](../science/01-model.md), equations (1.1)–(1.2) and the independence convention immediately following them.

### M03 — Phase uncertainty at a specified resolution

**Central question.** What can be said about the uncertainty of a phase law even when it has no probability density?

**Understanding target.** Form the equal-bin probabilities of an arbitrary Borel phase law and interpret their Shannon entropy $`H_m(\mu)`$. Explain why $`D_m(\mu)=\log_2m-H_m(\mu)`$ is the relative entropy of that histogram from a uniform one. Distinguish this discrete, resolution-dependent entropy from differential entropy.

**Dependencies and story role.** Uses M02. It supplies the classical quantity that will later approximate the quantum capacity.

**Conceptual connection.** Finite binning puts atomic, smooth, and singular continuous laws into the same finite probability space without asserting that the underlying laws are physically identical.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.1 and 10.5, “Entropy of a Random Variable” and “Relative Entropy”; [model](../science/01-model.md), “Angular entropy at a finite resolution,” equations (1.11)–(1.12).

### M04 — The transmitted system and its reference

**Central question.** Why is preserving an unknown quantum state a problem about correlations with another system?

**Understanding target.** Distinguish a joint state from either of its reduced states and explain the role of partial trace. Identify the inaccessible reference used to define entanglement transmission, and distinguish it from an auxiliary system available to an encoder or decoder.

**Dependencies and story role.** Uses M01–M02. It expands the local oscillator description into the composite-system setting needed to define quantum communication.

**Conceptual connection.** A channel can preserve some local probabilities while destroying the correlations that make quantum transmission successful.

**Source pointers.** [Wilde](anchor.md#states-and-reductions), §4.3, “Composite Noisy Quantum Systems,” and §24.1, “The Information-Processing Task”; [model](../science/01-model.md), “The charged resource,” including the entanglement-transmission convention around (1.4).

### M05 — Purification and equal reduced spectra

**Central question.** How can a mixed state be represented inside a pure state, and what does that representation say about entropy?

**Understanding target.** Explain purification and the equality of the nonzero spectra of the two reduced states of a pure bipartite state. Recognize that an auxiliary purification label can carry a Gram matrix without being the physical channel receiver.

**Dependencies and story role.** Uses M04. It provides the spectral identification that later permits a complementary entropy to be studied on a finite-dimensional label system.

**Conceptual connection.** A change in one representation of a state can expose its entropy without changing the operational meaning of the original channel.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §5.1, “Purification,” and §11.1, “Quantum Entropy”; [phase quantization](../science/02-phase-quantization.md), §3, especially the explanation of the $`C`$- and $`F`$-marginals following (P15).

### M06 — The environment as a complementary output

**Central question.** What information does the phase channel leave in its environment?

**Understanding target.** Interpret the isometry $`|n\rangle\mapsto|n\rangle|e_n\rangle`$ and the overlaps of its environment vectors. Explain why tracing out the oscillator gives an ensemble depending only on the number probabilities, and why the vectors need not be orthogonal for the map to be an isometry.

**Dependencies and story role.** Uses M02, M04, and M05. It gives a common description of the receiver channel and the information available to its environment.

**Conceptual connection.** Channel dilation translates phase averaging into a comparison between what remains at the receiver and what is recorded outside it.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §5.2, “Isometric Evolution”; [model](../science/01-model.md), “An arbitrary-measure dilation,” equations (1.5)–(1.6).

### M07 — Classical labels and quantum mixture entropy

**Central question.** Why is the entropy of an ensemble's label different from the entropy of the quantum state it prepares?

**Understanding target.** Distinguish $`H(p)`$ from $`S(\sum_np_n|e_n\rangle\langle e_n|)`$, especially when the environment states are nonorthogonal. Explain the entropy upper bound for a pure-state ensemble and the role of entropy concavity when several conditional states are mixed.

**Dependencies and story role.** Uses M03, M05, and M06. It establishes the entropy bookkeeping used in both the coherent-information formula and the photon-shell argument.

**Conceptual connection.** A classical uncertainty label may contain more information than its nonorthogonal quantum encoding makes distinguishable.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.1, 11.1, and 11.9, “Quantum Entropy Inequalities”; [model](../science/01-model.md), equations (1.7) and (1.10); [capacity theorem](../science/03-capacity.md), equation (3.11).

### M08 — Coherent information and a communication rate

**Central question.** How does an entropy difference become an achievable rate of quantum communication?

**Understanding target.** Relate coherent information to conditional quantum entropy and to entanglement transmission. Distinguish the coherent information of one specified input, optimization over inputs, and the operational capacity obtained from long blocks with vanishing error. Recognize that an achievable input rate alone does not establish an optimized converse.

**Dependencies and story role.** Uses M04–M07. It connects the entropy expressions to the communication task rather than treating them only as properties of states.

**Conceptual connection.** Direct coding results and converse bounds answer complementary questions about the same operational rate.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §§11.4–11.5, §13.5, and §§24.1, 24.3–24.5; [model](../science/01-model.md), the capacity definition around (1.4) and equations (1.7)–(1.8).

### M09 — Degradability and number-diagonal optimization

**Central question.** Which structure makes this channel's optimization simpler than that of a general quantum channel?

**Understanding target.** Explain the receiver-to-environment simulation obtained by measuring number and preparing $`|e_n\rangle`$. Explain why number dephasing leaves the complement unchanged while raising receiver entropy, making a number-diagonal input sufficient. Relate degradability to coherent-information concavity and the single-letter capacity structure.

**Dependencies and story role.** Uses M06–M08. It identifies the standard channel-theory reduction, before the infinite-dimensional energy hypotheses are checked.

**Conceptual connection.** A restriction on how much more the environment can know turns a regularized communication problem into a single-input optimization.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §§5.2 and 13.5; [model](../science/01-model.md), “An arbitrary-measure dilation” and “Why the single-letter formula is valid here.” The [related-work account](../references/related-work.md#generalized-dephasing-and-energy-constrained-coding) identifies the inherited generalized-dephasing and coding results.

### M10 — A mean-energy constraint in an infinite-dimensional space

**Central question.** What does a bound on mean photon number permit, and why are the relevant entropies still finite?

**Understanding target.** Distinguish an unconditional block-average energy budget from a maximum photon number. Explain why rare large photon numbers remain admissible. Relate the Gibbs partition function and the geometric-distribution entropy $`g(E)`$ to finiteness of the receiver and complementary entropies needed for the energy-constrained coding theorem.

**Dependencies and story role.** Uses M01, M07, and M09. It checks that the standard optimization reduction applies to the actual oscillator resource convention.

**Conceptual connection.** Infinite Hilbert-space dimension does not force infinite accessible entropy at fixed mean energy, but it creates a tail that a converse must control.

**Source pointers.** [Wilde](anchor.md#operational-quantum-capacity), §10.1 and §24.1 for the entropy and communication framework; [model](../science/01-model.md), equations (1.3)–(1.4) and (1.8)–(1.10). The research-level energy extension is [Wilde–Qi, Theorem 3](../references/related-work.md#generalized-dephasing-and-energy-constrained-coding), with its assumptions verified on the model page.

### M11 — Symmetry as an optimization tool

**Central question.** When does averaging an input over channel symmetries preserve or improve coherent information?

**Understanding target.** Connect covariance, unitary invariance of entropy, and concavity of coherent information. Explain how a finite Weyl average sends an input to the maximally mixed state, and why symmetry plus concavity can certify that input as optimal for a cyclic dephasing channel.

**Dependencies and story role.** Uses M02 and M07–M09. It supplies an exactly solvable comparison channel for the later phase-rounding argument.

**Conceptual connection.** Group averaging can remove an input optimization when the objective respects the group action and is concave.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §4.4 for channel maps and §13.5 for coherent information of a channel; [phase quantization](../science/02-phase-quantization.md), §4, equations (P18)–(P19), for the cyclic symmetry argument supplied here.

### M12 — Entropy change under a product interaction

**Central question.** What limits the entanglement that a bounded interaction $`A\otimes B`$ can create per unit time?

**Understanding target.** Interpret the dimension-independent rate bound in terms of the two operator norms, and understand why subtracting scalar identity terms changes only local unitaries. Recognize the Schmidt-coefficient and row/column estimates behind the bound, including why a finite system can interact with an infinite-dimensional environment without introducing a dimension factor.

**Dependencies and story role.** Uses M05 and M07. It introduces the imported quantitative tool that will turn phase resolution into a constant entropy error.

**Conceptual connection.** Interaction strength, rather than the total number of bath degrees of freedom, can control the entropy change relevant to the comparison.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§5.1 and 11.1 for the purification and entropy language; [phase quantization](../science/02-phase-quantization.md), Lemma P2, equations (P9)–(P13). The exact product-Hamiltonian bound is attributed to [Childs–Leung–Vidal](../references/related-work.md#the-product-hamiltonian-entropy-rate-bound-is-established), not to the textbook or to a new lemma invented by this project.

### M13 — Conditioning, refinement, and bounded information in an error label

**Central question.** How can a classical label control an entropy difference even when it is correlated with the quantity being described?

**Understanding target.** Explain entropy decomposition by a label, monotonicity under refinement of a partition, and upper bounds from bounded conditional support. Relate a bounded moment of an integer label to a bounded entropy, and recognize that these arguments do not require an independent error label.

**Dependencies and story role.** Uses M03, M07, and M10. It gathers the classical entropy tools that connect cutoff blocks to a mean-energy tail and coarse phase cells to Gaussian broadening.

**Conceptual connection.** The information cost of identifying a block or correcting a quantization error can stay bounded even when its set of possible values is infinite.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.2 and 10.7, “Conditional Entropy” and “Entropy Inequalities”; [capacity theorem](../science/03-capacity.md), equations (3.9)–(3.13); [bath and smoothing](../science/04-bath-and-smoothing.md), §2.1, equations (B4), (B10), and (B13), for the moment and partition bounds used here.

### M14 — The complete problem after the standard reductions

**Central question.** What remains to be determined once the channel, coding task, and energy constraint are all in place?

**Understanding target.** Integrate the independent-use model, hidden phase, energy convention, complementary ensemble, and degradability reduction into the optimization

```math
Q_\mu(E)=\sup_{\sum_nnp_n\le E}
\left[H(p)-S\!\left(\sum_np_n|e_n\rangle\langle e_n|\right)\right].
```

Identify why neither the entropy of a selected input nor a hard-cutoff calculation yet evaluates this supremum uniformly over all phase laws.

**Dependencies and story role.** Integrates M01–M13. It closes the background phase with the full problem and the distinct tools available for its solution.

**Conceptual connection.** Textbook quantum communication becomes a specific infinite-dimensional optimization whose remaining difficulty is quantitative, including its high-photon tail.

**Source pointers.** [Wilde](anchor.md#operational-quantum-capacity), §§13.5, 24.1, 24.3, and 24.5; [model](../science/01-model.md), equation (1.8) and “Angular entropy at a finite resolution”; [scientific reading route](../science/README.md), “The proof dependencies.”

## Phase II — Narrative and innovation: M15–M30

### M15 — What phase rounding must preserve

**Central question.** What comparison is strong enough to turn a phase histogram into an optimized capacity bound?

**Understanding target.** State the desired comparison for every number distribution supported on $`d`$ consecutive levels. Distinguish a bound on the complementary entropy from a claim of small channel distance, and distinguish input-uniform control from an estimate only for a flat input. Explain the choice of $`d`$ phase bins and their midpoints.

**Dependencies and story role.** Uses M03, M08, M10, M12, and M14. It starts the narrative with the local quantity the new argument must control.

**Conceptual connection.** The resolution scale $`1/d`$ becomes useful only after its approximation error is controlled in the operational entropy expression.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§11.10 and 13.5 for entropy continuity and coherent information; [phase quantization](../science/02-phase-quantization.md), Theorem P1 and equations (P7)–(P8), with the direct-entropy interpretation following (P17).

### M16 — Put the two complementary states in one purification space

**Central question.** How can the original phase law and its rounded version be compared without changing their environment spaces?

**Understanding target.** Explain the common space $`C\otimes L^2(\mu)`$, the two sets of phase functions, and their Gram matrices. Identify the reduced states whose entropies equal the complementary-output entropies. Keep the auxiliary label system $`C`$ distinct from the physical receiver, whose diagonal output remains $`\rho_p`$.

**Dependencies and story role.** Uses M05–M07 and M15. It constructs the mathematical comparison on which the bounded entropy change will act.

**Conceptual connection.** Purification converts a comparison of two channels into a controlled transformation between two pure states representing their environments.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§5.1–5.2 and §11.1; [phase quantization](../science/02-phase-quantization.md), §3, equations (P14)–(P16) and the marginal-state explanation following (P15).

### M17 — Why the rounding error costs only a constant

**Central question.** Why does finer phase resolution prevent the entropy comparison from growing with the cutoff dimension?

**Understanding target.** Identify the residual interaction $`N_C\otimes R`$ and center the number generator. Explain how the number range of order $`d`$ and residual phase norm of order $`1/d`$ give $`C_d\le C`$ through the product-interaction rate bound. Recognize that the estimate is uniform in both the input distribution and the phase law.

**Dependencies and story role.** Uses M12 and M16. This is the central entropy-comparison mechanism.

**Conceptual connection.** A bound on entanglement generation becomes an input-uniform information bound for a noisy communication channel.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§5.1 and 11.1 for the underlying entropy representation; [phase quantization](../science/02-phase-quantization.md), equations (P14)–(P17), with Lemma P2 as the explicitly attributed research ingredient.

### M18 — Solve the grid channel and obtain the cutoff theorem

**Central question.** How does the rounded phase law turn the entropy comparison into matching capacity bounds?

**Understanding target.** Combine the cyclic-channel symmetry with orthogonality of its phase-error Choi vectors to obtain the exact rounded value $`D_d(\mu)`$. Transfer that value through the uniform comparison to both the flat-input lower bound and the arbitrary-input cutoff upper bound. Interpret the flat-input Toeplitz entropy relation as a consequence within this broader result.

**Dependencies and story role.** Uses M11 and M15–M17. It assembles the local comparison into the first complete capacity statement, still under a hard cutoff.

**Conceptual connection.** An exactly solvable finite channel can bound a general phase channel once the comparison preserves the right entropy uniformly over inputs.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §§5.2, 11.1, and 13.5; [phase quantization](../science/02-phase-quantization.md), Theorem P1, equations (P18)–(P21); [capacity theorem](../science/03-capacity.md), equation (3.5).

### M19 — Move a photon block without changing its coherent information

**Central question.** Why can a block of large photon numbers be compared with a block of the same length beginning at zero?

**Understanding target.** Explain why a common number shift changes neither the probability entropy nor the complementary entropy: multiplication by $`e^{-ia\theta}`$ is one environment unitary. Distinguish this entropy invariance from an assertion that the original block has become free of its energy cost.

**Dependencies and story role.** Uses M06, M07, and M18. It makes the cutoff estimate applicable to every consecutive block in the unbounded photon distribution.

**Conceptual connection.** Absolute photon number affects the charged energy, while coherent information within a block depends on the relative number differences.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§4.4 and 11.1 for unitary invariance; [capacity theorem](../science/03-capacity.md), “A photon-number shift does not change coherent information,” equation (3.6).

### M20 — The entire high-photon tail has a bounded shell cost

**Central question.** How can a mean-energy constraint control arbitrarily large photon numbers without discarding them?

**Understanding target.** Interpret the dyadic shell label $`K(n)=\lfloor\log_2(1+n/m)\rfloor`$ and the shell length $`m2^k`$. Explain why the mean-energy budget bounds both $`\mathbb EK`$ and $`H(K)`$, and how the classical chain rule and quantum entropy concavity separate the within-shell contribution from the label cost.

**Dependencies and story role.** Uses M10, M13, and M19. It supplies the step that a hard-cutoff proof alone cannot provide.

**Conceptual connection.** A rare event may have a large photon number while contributing only a bounded amount of information about which geometric energy scale was used.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.2, 10.7, and 11.9; [capacity theorem](../science/03-capacity.md), “Dyadic shells control the whole energy tail,” equations (3.7)–(3.12), including the finiteness justification after (3.11).

### M21 — Assemble the universal mean-energy capacity theorem

**Central question.** Why can neither an unusual photon distribution nor a rare high-energy component beat the histogram estimate by an unbounded amount?

**Understanding target.** Combine shell costs, photon-shift invariance, and exact refinement of phase bins to obtain the optimized upper bound. Match it to a feasible flat-number input and interpret

```math
D_m(\mu)-C\le I_c(u_m,\mathcal N_\mu)
\le Q_\mu(E)\le D_m(\mu)+C+3,
\qquad m=\lceil E\rceil.
```

Distinguish a universal additive guarantee from an optimal constant, an efficient encoder, or a finite-block error formula.

**Dependencies and story role.** Uses M13 and M18–M20. It closes the main proof and identifies the full operational content of the theorem.

**Conceptual connection.** Uniform local entropy control and a bounded global label cost together evaluate the original infinite-dimensional optimization.

**Source pointers.** [Wilde](anchor.md#operational-quantum-capacity), §§24.3–24.5 for the direct/converse distinction; [capacity theorem](../science/03-capacity.md), Theorem 1, equations (3.2)–(3.4) and (3.13)–(3.14).

### M22 — Information dimension as a capacity consequence

**Central question.** What does the growth of phase-histogram entropy imply about the growth of quantum capacity?

**Understanding target.** Relate lower and upper information dimensions to the corresponding reversed upper and lower capacity prelogs. Explain why the finite-resolution theorem still applies if the dimension limit does not exist, and why a zero logarithmic coefficient does not imply zero or bounded capacity.

**Dependencies and story role.** Uses M03 and M21. It extracts an asymptotic interpretation while preserving the stronger finite-resolution statement.

**Conceptual connection.** Classical resolution-dependent uncertainty determines the fraction of the logarithmic photon information budget that remains available for quantum communication.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.1 and 10.5 for histogram entropy and its deficit; [capacity theorem](../science/03-capacity.md), equations (3.15)–(3.16); [related work](../references/related-work.md#information-dimension-and-physical-phase-laws) for the inherited information-dimension definition and its attribution.

### M23 — Realize the phase law with a bounded spin bath

**Central question.** How can a geometric family of phase laws arise from a physical pure-dephasing interaction?

**Understanding target.** Connect independent bath-spin labels to the phase sum $`X_K=(r-1)\sum_{k=1}^K B_kr^{-k}`$. Explain the oscillator-number coupling, absolute summability, and bounded bath observable. Distinguish stationarity of a bath state from independence between channel uses, and identify where fresh preparation or independent resetting enters.

**Dependencies and story role.** Uses M01, M02, M06, M10, and M21. It moves from an arbitrary mathematical phase law to a finite physical family with explicit resource and memory assumptions.

**Conceptual connection.** An environment spectrum supplies a classical phase distribution, but the communication model also depends on how that environment is prepared across uses.

**Source pointers.** [Wilde](anchor.md#channels-and-environments), §§4.5 and 5.2 for channel interpretation and isometric evolution; [bath and smoothing](../science/04-bath-and-smoothing.md), equations (B18) and (B25)–(B26), §6; [related work](../references/related-work.md#information-dimension-and-physical-phase-laws) for the Ben Attar–Bar-Gill antecedent.

### M24 — Count the bath information visible at a finite resolution

**Central question.** How many independent spin labels can a phase histogram resolve before the finite bath is exhausted?

**Understanding target.** Explain the separated-prefix intervals and the bounded intersection counts behind $`H_m(\mu_K)=\min\{K,\delta\log m\}+O_r(1)`$, with $`\delta=1/\log_2r`$. Relate the first resolved spins to the fractional capacity coefficient and complete resolution of a finite bath to a fixed entropy deficit.

**Dependencies and story role.** Uses M03, M13, M22, and M23. It evaluates the main theorem for the bath family with an error uniform in bath size.

**Conceptual connection.** The histogram reveals successive scales of an environmental spectrum, and each resolved fair spin contributes one bit of phase uncertainty.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.1–10.2 for entropy of labels and conditioning; [bath and smoothing](../science/04-bath-and-smoothing.md), Proposition B3, equations (B19)–(B22), and the unsmoothed case of (B23).

### M25 — Gaussian broadening changes fine-bin entropy in a controlled way

**Central question.** How does independent continuous phase noise alter the entropy resolved by an arbitrary histogram?

**Understanding target.** Distinguish coarse bins with $`ms\le1`$ from fine bins with $`ms\ge1`$. Explain the bounded-entropy quantization error in the first regime and the additional $`\log(ms)+O(1)`$ uncertainty in the second. Account for the winding index on the circle, the coarse-label estimator, and the difference between cycles and radians.

**Dependencies and story role.** Uses M03, M13, and M21. It establishes a smoothing statement for every Borel phase law, independently of the geometric-bath example.

**Conceptual connection.** A continuous perturbation can remove a singular distribution's arbitrarily fine structure while leaving coarser histogram information stable to a bounded entropy error.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§10.2 and 10.7 for the conditioning framework; [bath and smoothing](../science/04-bath-and-smoothing.md), Theorem B1 and §§2.1–2.3, equations (B3)–(B14). The differential-entropy and moment steps are supplied on that page rather than assumed from an unverified textbook section.

### M26 — The smaller of photon resolution and noise resolution governs capacity

**Central question.** Why does a fixed amount of smooth phase broadening eventually stop unbounded capacity growth?

**Understanding target.** Insert the general smoothing identity into the capacity theorem and explain the cancellation of the extra fine-bin entropy against the logarithmic number budget. Identify $`F=\min\{E,1/s\}`$ as the useful resolution, with rounding handled by bounded partition comparisons. Relate the resulting plateau to the known unrestricted-energy formula for the resulting smooth density.

**Dependencies and story role.** Uses M13, M21, and M25. It converts the classical smoothing lemma into a general communication consequence.

**Conceptual connection.** More photons can reveal more phase detail, but below the continuous-noise width that detail costs as much entropy as the increased information budget supplies.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §§10.5 and 13.5 for entropy deficit and coherent information; [bath and smoothing](../science/04-bath-and-smoothing.md), Corollary B2, equations (B15)–(B17); [related work](../references/related-work.md#exact-unconstrained-capacity-for-phase-densities) for the qualified Lami–Wilde density-law result.

### M27 — Combine finite bath size, smoothing, and the order of limits

**Central question.** Which physical scale determines whether the capacity shows fractional growth, full logarithmic growth, or saturation?

**Understanding target.** Interpret the unified law

```math
Q_{\mu_K*G_s}(E)
=\log F-\min\{K,\delta\log F\}+O_r(1),
\qquad F=\min\{E,1/s\},
```

with $`F=E`$ when there is no broadening. Explain how the relative sizes of $`E`$, $`r^K`$, and $`1/s`$ select the regimes, and why finite-$`K`$, infinite-$`K`$, and fixed-positive-$`s`$ energy limits differ. Distinguish a bounded-error growth law from a sharp crossover or a pointwise slope.

**Dependencies and story role.** Integrates M22–M26. It brings the physical consequences into one parameter-dependent picture.

**Conceptual connection.** Finite environment size and continuous background noise impose different limits on the amount of phase structure that a photon budget can use.

**Source pointers.** [Wilde](anchor.md#coherent-information-and-degradability), §§10.1 and 13.5 for the underlying entropy/rate quantities; [bath and smoothing](../science/04-bath-and-smoothing.md), equations (B23)–(B24) and the regime table; [interpretation](../science/05-interpretation.md#the-three-resolution-regimes-of-a-geometric-bath).

### M28 — Read the finite calculations as evidence with a defined scope

**Central question.** What does the numerical Toeplitz calculation verify, and what remains supplied by the analytic proof?

**Understanding target.** Interpret the plotted value $`\log_2d-S(T_d/d)`$ as flat-input coherent information at mean photon number $`(d-1)/2`$. Distinguish a rigorous infinite-product truncation estimate from floating-point diagnostics and saved-reference agreement. Explain why the finite curves neither optimize capacity nor establish an asymptotic exponent.

**Dependencies and story role.** Uses M05, M08, M18, M21, and M27. It connects the proved mechanisms to the bounded numerical evidence without extending the evidence beyond its task.

**Conceptual connection.** Numerical calculations check conventions and illustrate regimes; input-uniform and full-tail claims require the corresponding proofs.

**Source pointers.** [Wilde](anchor.md#entropy-and-conditional-information), §§11.1, 11.10, and 13.5; [verification guide](../verification/README.md), including the exact endpoints and analytic tail bound; [recorded run](../verification/last-run.txt); [interpretation](../science/05-interpretation.md#what-the-finite-calculations-show).

### M29 — Locate the contribution among its established ingredients

**Central question.** Which part of the scientific conclusion is added by the uniform optimized bound?

**Understanding target.** Separate the inherited coding reduction, product-Hamiltonian entangling rate, uniform-orbit spectral-entropy mechanism, density-law capacity results, and geometric bath construction from the input-uniform comparison and mean-energy evaluation. Explain why a prescribed-input entropy slope or a variational capacity formula does not already give the complete universal additive estimate.

**Dependencies and story role.** Uses M14, M17–M18, M21–M22, and M23–M27. It places the assembled result in its actual mathematical and physical lineage.

**Conceptual connection.** A contribution can join established tools into a stronger operational conclusion without making those tools or their earlier physical mechanisms new.

**Source pointers.** [Wilde](anchor.md#operational-quantum-capacity), §§13.5 and 24.3–24.5 for the standard capacity framework; [related work](../references/related-work.md), especially “Capacity theory inherited from earlier work” and “Entropy and Toeplitz results: what transfers and what remains”; [interpretation](../science/05-interpretation.md#information-dimension-is-a-consequence-not-an-extra-hypothesis).

### M30 — Synthesis: the physical meaning and reach of the theorem

**Central question.** What can the complete argument tell us about quantum communication through a specified phase environment at a specified photon budget?

**Understanding target.** Integrate the channel and resource assumptions, the finite-resolution entropy deficit, the optimized converse, the simple near-optimal input spectrum, and the finite-bath/smoothing regimes. Explain why the theorem covers arbitrary Borel phase laws while remaining a statement about independent, known-law, pure-dephasing communication. Preserve the boundaries concerning bath reuse, photon loss, singular-law assistance, strong converses, finite-block errors, and encoder complexity.

**Dependencies and story role.** Integrates M14 and M21–M29. It closes the narrative with the full scientific claim, its meaning, and the assumptions under which its consequences follow.

**Conceptual connection.** The classical phase information resolved at the photon scale and the quantum information recoverable over many channel uses are linked by one optimized, bounded-error law.

**Source pointers.** [Wilde](anchor.md#operational-quantum-capacity), §§24.1 and 24.3–24.5 for the operational task and theorem structure; [main theorem](../science/03-capacity.md#main-theorem); [physical crossover](../science/04-bath-and-smoothing.md#5-capacity-crossover-with-finite-bath-size-and-broadening); [interpretation and scope](../science/05-interpretation.md).
