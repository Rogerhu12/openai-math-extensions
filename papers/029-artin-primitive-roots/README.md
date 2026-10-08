# 029 — Primitive-root density and Hecke zero-free regions

**Research draft** · three manuscripts:

| Manuscript | Files |
| --- | --- |
| Positive lower density of primitive-root primes | [PDF](artin_positive_density.pdf) · [TeX](artin_positive_density.tex) |
| A seven-eighths theorem for Hecke characters over arbitrary number fields | [PDF](hecke_seven_eighths_all_characters.pdf) · [TeX](hecke_seven_eighths_all_characters.tex) |
| A common zero-free strip for Hecke $`L`$-functions | [PDF](hecke_zero_free_strip.pdf) · [TeX](hecke_zero_free_strip.tex) |

## Results and comparison with OpenAI 029

An integer $`a`$ is admissible if it is neither $`-1`$ nor an integer square. Let $`A_a(x,2x)`$ count primes $`x<p\le2x`$ with $`p\nmid a`$ and $`\operatorname{ord}_p(a)=p-1`$.

The comparison below uses Theorems 1.1 and 1.2 of the [pinned OpenAI 029 paper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf). The conclusions in this collection depend on the analytic inputs listed below.

| Result | OpenAI 029 | This collection |
| --- | --- | --- |
| Primitive-root primes | $`A_a(x,2x)\gg_a x/(\log x)^2`$ for each admissible $`a`$ | $`A_a(x,2x)\gg_a x/\log x`$, and positive lower relative density among primes |
| Common Hecke zero-free region | Width $`10^{-6}`$ for finite-order Hecke characters over cyclotomic fields containing $`\mu_{12}`$ | $`\Re s>7/8`$ for every unitary Hecke character, of finite or infinite order, over every number field; independently, width $`25/258`$ for finite-order characters |

The **seven-eighths paper** gives $`L_F(s,\psi)\ne0`$ for $`\Re s>7/8`$ for every number field $`F`$ and every continuous unitary Hecke character $`\psi`$, with arbitrary infinity type; a pole of a unitary norm character is permitted. The boundary is independent of the field, conductor, infinity type and height; implied constants are not uniform in these data. The proof passes to $`K=F(\zeta_{12})`$, closes over the family of finite-order twists of one fixed character and its conjugate (first $`11/12`$, then $`7/8`$), and descends to $`F`$ by abelian factorization.

The **width-$`25/258`$ paper** gives $`L_K(s,\chi)\ne0`$ for $`\Re s>233/258`$, allowing the usual pole at one for the principal character. The width is common to all fields and characters; implied constants may depend on the fixed field, character, and local data. Its exact variational endpoint is slightly stronger:

```math
\Delta_\#=0.096906264531643757\ldots.
```

The **Artin paper** uses primes whose predecessor has a single large prime factor. For any available common width $`0<\delta<1/2`$, it proves

```math
\liminf_{X\to\infty}\frac{A_a(X)}{\pi(X)}
\ge \alpha_a(Y)[-\log(1-\delta)]-\tau(Y),
```

where $`A_a(X)`$ counts primitive-root primes up to $`X`$, $`\alpha_a(Y)\asymp_a1/\log Y`$ is the explicit congruence-class proportion, and $`\tau(Y)\le1/Y`$ is the splitting tail. The bound also holds for $`\liminf_{x\to\infty}A_a(x,2x)\log x/x`$ and is positive for all sufficiently large fixed $`Y`$. Either Hecke paper supplies an admissible width: $`\delta=1/8`$ or $`\delta=25/258`$. The conclusion is a positive lower relative density, not existence of a natural density or the full Artin asymptotic.

## Mathematical dependencies

The seven-eighths proof uses the theta construction and local identities of **OpenAI 029, Sections 3 and 5–7 and Appendix A**, and the physical estimates, zero detection and canonical moment arguments of [OpenAI 003](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), **Sections 4–20**. Its Section 3 and Appendix A supply the transfer of these constructions to a general field containing $`\mu_{12}`$ and to a fixed unitary infinity type. The long original canonical proofs are used as source inputs and are not re-proved line by line.

The width-$`25/258`$ proof uses different inputs and does not depend on the seven-eighths paper. The Hecke proof uses the theta realization, reflected expansion, and estimates from **OpenAI 029, Sections 3–8 and Appendix A**, together with A. de Faveri's fixed-order large sieve, [arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1). Its first section states the inputs used and applies them over a fixed number field.

The Artin proof uses a common Hecke strip and the one-sided marked Type II and two-sided correlation estimates from **Sections 3 and 6** of [The Poisson–Dirichlet Law for Prime Predecessors](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf), including the graph estimates used in their proofs, together with **OpenAI 029, Lemma 10.2**. The stated invariance under removing powers of marking primes and the allowed divisor growth are retained. The appendix derives the required single-large-factor statistic in fixed arithmetic progressions from these inputs.

## Numerical certificate

The Hecke appendix's [optimized-endpoint certificate](certificates/hecke_double_sparse_endpoint_certificate.py) checks its numerical enclosure by exact rational arithmetic; the [recorded output](certificates/hecke_double_sparse_endpoint_certificate_results.txt) is included. The computation does not verify the analytic inputs. The rational width and exact variational definition are independent of the numerical enclosure.
