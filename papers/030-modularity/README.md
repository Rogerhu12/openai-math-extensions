# 030 — Modularity of elliptic curves over CM and totally real fields

**Research draft** · [PDF](modularity_cm_totally_real.pdf) · [TeX](modularity_cm_totally_real.tex)

[OpenAI 030](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf) proves that every elliptic curve over an imaginary quadratic field is modular. This manuscript runs its geometric prime-switching argument over more general base fields.

## Main results

Assume the geometric and local assertions of OpenAI 030, in the form specified in Section 2 of this manuscript.

- **Totally real fields.** Every elliptic curve over a totally real number field is modular (Corollary 6.1).
- **CM fields without $`\zeta_5`$.** Every elliptic curve over a CM field $`K`$ with $`\zeta_5\notin K`$ is modular, with no Galois or degree restriction on $`K`$ (Theorem 5.1).
- **CM fields with $`\zeta_5`$.** The same conclusion holds if, in addition, the proposed exceptional-five lifting argument of Proposition 10.1 is valid (Corollary 13.1). Proposition 10.1 is an ordinary automorphy-lifting statement for residual image $`\mathrm{SL}_2(\mathbb F_5)`$ under split Tate local conditions whose parameter valuations are prime to five.

The first two results do not use Proposition 10.1. Independently of OpenAI 030's geometry, Proposition 10.1 would also remove the condition $`\zeta_5\notin K`$ from Caraiani–Newton's mod-three modularity criterion (Corollary 14.1).

## What changes from OpenAI 030

In OpenAI 030 the imaginary quadratic hypothesis is used to guarantee $`\zeta_5\notin K(\mu_{3p})`$ (equation (5.2) there), which is needed for the mod-five starting point. Here:

- the auxiliary elliptic curve $`A_t`$ that starts the chain of congruences is shown to be defined over $`K`$ itself, so the mod-five starting point only needs $`\zeta_5\notin K`$ (Sections 2 and 5);
- the large-image prime $`p`$ and the decomposed-genericity conditions are chosen uniformly over all conjugates of $`K`$, using its normal closure (Sections 3–4);
- the totally real case follows by quadratic descent from a suitable CM extension (Section 6).

## Dependencies

Section 2 lists the OpenAI 030 inputs used over these more general base fields:

- Covers and rank-two compatible systems: Lemma 3.1 and Propositions 5.1–5.2.
- Integral character congruences and monodromy: Proposition 4.2, Theorem 4.5, Lemma 5.3, and Corollary 5.4.
- Local specialization and automorphic local comparison: Proposition 7.5, Corollary 7.6, and Lemma 9.2.
- For CM fields containing $`\zeta_5`$, the second degeneration: Lemmas 3.2 and 3.5 and equation (3.7), with the width-three calculation in Section 12 of this manuscript.

The automorphy steps use Caraiani–Newton, [Theorems 5.2](https://arxiv.org/html/2301.10509v3#S5.SS2) and [6.1](https://arxiv.org/html/2301.10509v3#S6.SS1), and Lemma 6.1.3; base change and descent use [Allen et al., Proposition 6.5.13](https://arxiv.org/abs/1812.09999).
