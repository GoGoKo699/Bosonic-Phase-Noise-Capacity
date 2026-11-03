# Learning the capacity argument

[Project overview](../README.md) · [Scientific account](../science/README.md)

An oscillator can carry quantum information in superpositions of photon-number states. Phase noise changes their relative phases without changing the number probabilities. The question is how much quantum information can still be transmitted when only the mean photon number is limited. The answer depends on how much phase uncertainty is visible at the resolution supplied by that budget.

The route uses **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)** as its single educational anchor. Its states, channels, entropy and coding framework leads to the project's energy-constrained optimization. The [source bridge](anchor.md) supplies the additional oscillator and proof steps, with research-level ingredients attributed to their primary papers.

## Start with a complete example

[Two phases, two encodings](two-phase-example.md) follows an oscillator that receives either no rotation or a half-turn. An encoding in neighboring number states loses its coherence; an encoding using two even number states preserves it. The same example gives an exact four-level coherent-information calculation and makes the photon cost explicit. It provides a concrete entry to milestones M01–M09 and the cutoff comparison in M15–M18.

## Follow the project map

The [30-milestone map](milestones.md) has two phases. **M01–M14** connect the carrier, phase law, subsystem states, entropy, coding and energy into the complete capacity optimization. **M15–M30** connect the rounding mechanism, cyclic comparison and photon-shell converse to the theorem, physical examples, numerical evidence and final interpretation. The allocation follows the scientific argument and is common to every reader.

| Reading goal | Route |
|---|---|
| Understand the physical question and the relevant entropy difference | [Worked example](two-phase-example.md), then M01–M09 |
| See exactly how Wilde's framework reaches the oscillator problem | [Anchor and source bridge](anchor.md), then M10–M14 |
| Follow the two decisive proof mechanisms | M15–M21, with [phase quantization](../science/02-phase-quantization.md) and the [mean-energy converse](../science/03-capacity.md) |
| Interpret finite baths, continuous noise and numerical curves | M22–M30, with [bath and smoothing](../science/04-bath-and-smoothing.md) and [verification](../verification/README.md) |

Each milestone states a central question, an understanding target, earlier dependencies, its role in the argument and source pointers. M14 assembles the background into the optimization problem; M30 assembles the full scientific conclusion. The map gives a connected understanding of the work while leaving specialist calculations in their authoritative science pages.

## Keep the central distinctions in view

A mean-energy budget permits photon-number tails; a hard cutoff removes them. A coherent-information value for one input supplies an achievable rate; an optimized converse bounds every admissible input. The finite phase histogram is a classical probability distribution; the complementary state is a quantum mixture whose component states may overlap. These distinctions explain why both the uniform phase comparison and the full-tail argument are needed.

The [source bridge](anchor.md#the-missing-bridges) marks which steps come from the textbook, which use imported research theorems and which are proved in this project. Specialists can proceed directly to the [canonical model and proofs](../science/README.md).
