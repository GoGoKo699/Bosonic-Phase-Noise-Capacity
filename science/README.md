# Scientific reading route

The central question is how the mean photon number controls quantum communication through an oscillator with an arbitrary phase-noise distribution. The result identifies a finite angular resolution at which an ordinary classical entropy determines the optimized quantum rate to a universal additive error.

## Follow the argument

1. [The model and coding problem](01-model.md) fixes the independent-use channel, the average input-energy convention, arbitrary-Borel dilation and inherited single-letter capacity formula.
2. [Phase quantization](02-phase-quantization.md) proves that rounding the phase to a grid changes the relevant entropy by only a constant, uniformly over every input supported on consecutive photon-number levels. It also identifies the finite cyclic channel's exact optimum.
3. [The capacity theorem](03-capacity.md) partitions an arbitrary admissible input into photon-number shells, controls the entire mean-energy tail, and derives the information-dimension consequences.
4. [Finite baths and smooth noise](04-bath-and-smoothing.md) proves the Gaussian quantization identity and the geometric spin-bath law. Together they show how bath size and background broadening determine the useful resolution range.
5. [Interpretation and boundaries](05-interpretation.md) explains the operational consequence, the exact role of the known ingredients, and the differences between this theorem and a claim about code complexity or a noisy memory channel.

The [related-work account](../references/related-work.md) records the closest primary comparisons. The [verification route](../verification/README.md) separates numerical convention checks from the general proof.

## The proof dependencies

The coding reduction uses degradability and the energy-constrained coding theorem of Wilde and Qi. The phase-rounding comparison uses the dimension-independent product-interaction entangling rate of Childs, Leung and Vidal. Coherent-information concavity and finite cyclic covariance then solve the rounded optimization. The final shell argument is what converts a cutoff statement into a mean-energy capacity bound. The quantitative constants and the allowed tails are stated in the [main theorem](03-capacity.md#main-theorem).

The bath and smoothing consequences depend only on that theorem and the explicitly proved entropy estimates on their page. They do not require exact Fourier decay, an ideal infinite bath, or a claimed persistence of a fractal slope under fixed smooth noise.
