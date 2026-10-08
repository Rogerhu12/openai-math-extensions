# 159 — A single-exponential progression exponent

**Research draft** · [PDF](math159_one_level_bound.pdf) · [TeX](math159_one_level_bound.tex)

## Main result

For each integer $`k\ge3`$, let $`r_k(N)`$ be the largest size of a subset of $`\{1,\ldots,N\}`$ containing no nonconstant $`k`$-term arithmetic progression. Under the dependencies below, Theorem 1.1 gives an absolute constant $`C>0`$ such that

```math
r_k(N)\le K_kN\exp[-c_k(\log N)^{\varepsilon_k}],
\qquad \varepsilon_k=\exp(-k^C),
\qquad N\ge3.
```

The exponent has single-exponential dependence on the progression length $`k`$. The absolute constant $`C`$ and the positive constants $`K_k,c_k`$ are not given numerical values. Section 5 derives the density bound from the estimates in Sections 2–4.

## Comparison with OpenAI 159

The main theorem of [OpenAI 159](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) gives the same form of progression bound for some $`\varepsilon_k>0`$, without specifying its dependence on $`k`$. This manuscript obtains $`\varepsilon_k=\exp(-k^C)`$ by modifying the degree and parameter estimates.

## Depends on

- **OpenAI 159's analytic inputs.** Section 1 of this manuscript lists the following inputs from OpenAI 159: the absolute-patch theorem (Lemma 2.2), the sampler and rank-transfer estimates (Sections 3–4 and Appendices F–H), the field and active-return framework (Definition 8.1 and Theorem 8.2), exact extraction (Section 9), and the compression and descending numerical schedule (Section 10).
- **The inverse-theorem argument and quantitative nilsequence estimates.** Section 4.1 of this manuscript modifies the quantitative induction in [Leng–Sah–Sawhney, arXiv:2402.17994v3](https://arxiv.org/html/2402.17994v3), using [Leng, arXiv:2312.10772v5](https://arxiv.org/html/2312.10772v5). It also uses the additive-combinatorial and fixed $`U^3`$ base-case results of Sanders, Milićević, Leng, and Jamneshan–Tao cited there. The single-exponential parameter estimate is derived in this manuscript.

The additional algebraic and quantitative arguments are given in Sections 2–4. [Pinned references](../../docs/SOURCES.md) record the upstream versions.

