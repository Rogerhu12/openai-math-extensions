# 159 — A single-exponential progression exponent

**Research draft** · [PDF](math159_single_exponential.pdf) · [TeX](math159_single_exponential.tex)

This 23-page manuscript, dated 8 October 2026, replaces the earlier `math159_one_level_bound` draft. The earlier draft omitted a chain of inverse-theorem calls; the replacement treats supplied-derivative integration in Section 4.4 and relative detection by cube-degree descent in Section 5. The earlier files remain in the Git history.

## Main result

For each integer $`k\ge3`$, let $`r_k(N)`$ be the largest size of a subset of $`\{1,\ldots,N\}`$ containing no nonconstant $`k`$-term arithmetic progression. Under the dependencies below, Theorem 1.1 gives an absolute constant $`C>0`$ such that

```math
r_k(N)\le K_kN\exp[-c_k(\log N)^{\varepsilon_k}],
\qquad \varepsilon_k=\exp(-k^C),
\qquad N\ge3.
```

The exponent has single-exponential dependence on the progression length $`k`$. The absolute constant $`C`$ and the positive constants $`K_k,c_k`$ are not given numerical values. Section 7 derives the density bound from the geometric and analytic modifications in Sections 2–6.

## Comparison with OpenAI 159

The main theorem of [OpenAI 159](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) gives the same form of progression bound for some $`\varepsilon_k>0`$, without specifying its dependence on $`k`$. This manuscript obtains $`\varepsilon_k=\exp(-k^C)`$ by modifying the degree and parameter estimates.

## Depends on

- **OpenAI 159's analytic inputs.** Section 1 of this manuscript lists the absolute-patch theorem (Lemma 2.2), the sampler and rank-transfer contracts (Sections 3-4 and Appendices F-H), the comparison and exact-marking framework (Sections 5-8 and Appendices A-E and I), extraction (Section 9), and the density-increment construction and parameter order (Section 10). Their analytic conclusions and prescribed dependencies of warm bounds are retained.
- **The inverse-theorem argument and quantitative nilsequence estimates.** Section 4 of this manuscript gives an additional order-dependent budget calculation for the proof of [Leng-Sah-Sawhney, arXiv:2402.17994v3](https://arxiv.org/html/2402.17994v3), using [Leng, arXiv:2312.10772v5](https://arxiv.org/html/2312.10772v5). Proposition 4.5 gives the supplied-derivative integration statement, and Section 5 treats cube completion and relative detection.

The additional algebraic and quantitative arguments are given in Sections 2–6. The proof is relative to the listed source framework and does not independently verify all of its analytic arguments. [Pinned references](../../docs/SOURCES.md) record the upstream versions.

