# Extensions of results in OpenAI/math

[中文说明](README.zh-CN.md)

AI-assisted research drafts; see [AI disclosure](NOTICE.md). This collection is independent of OpenAI/math.

Every result below is conditional on the inputs in its last column. None has been refereed or formally verified.

## Papers

| Family | OpenAI result | Extension | Depends on |
| --- | --- | --- | --- |
| [017](papers/017-rational-logarithms/) · [PDF](papers/017-rational-logarithms/log-rational-irrationality-proof.pdf) | $`\mu(\pi)=2`$ | $`\mu(\log a)=2`$ for every rational $`a>0`$, $`a\ne1`$ | OpenAI 017, Lemma 2.2 |
| [029](papers/029-artin-primitive-roots/) · [Artin PDF](papers/029-artin-primitive-roots/artin_positive_density.pdf) · [Hecke $`7/8`$ PDF](papers/029-artin-primitive-roots/hecke_seven_eighths_all_characters.pdf) · [Hecke $`25/258`$ PDF](papers/029-artin-primitive-roots/hecke_zero_free_strip.pdf) | For each admissible $`a`$, $`\gg_a x/(\log x)^2`$ primitive-root primes in $`(x,2x]`$; Hecke zero-free width $`10^{-6}`$ over cyclotomic fields containing $`\mu_{12}`$ | $`\gg_a x/\log x`$, i.e. positive lower relative density. Every unitary Hecke character over every number field, of finite or infinite order, has $`L(s,\psi)\ne0`$ for $`\Re s>7/8`$; an independent route gives width $`25/258`$ for finite-order characters | [$`7/8`$: OpenAI 003 and 029 constructions transferred to general fields; $`25/258`$: OpenAI 029 and de Faveri's large sieve; Artin: prime-predecessor estimates](papers/029-artin-primitive-roots/#mathematical-dependencies) |
| [030](papers/030-modularity/) · [PDF](papers/030-modularity/modularity_cm_totally_real.pdf) | Elliptic curves over imaginary quadratic fields are modular | Elliptic curves over every totally real field, and over every CM field $`K`$ with $`\zeta_5\notin K`$, are modular. Over CM fields containing $`\zeta_5`$, the same holds assuming Proposition 10.1 | [OpenAI 030's geometric and local inputs](papers/030-modularity/#dependencies); for CM fields containing $`\zeta_5`$, also the proposed lifting argument of Proposition 10.1 |
| [159](papers/159-szemeredi-exponents/) · [PDF](papers/159-szemeredi-exponents/math159_one_level_bound.pdf) | $`r_k(N)\le K_kN\exp[-c_k(\log N)^{\varepsilon_k}]`$ for some $`\varepsilon_k>0`$, dependence on $`k`$ unspecified | The same bound with $`\varepsilon_k=\exp(-k^C)`$, $`C`$ absolute | [OpenAI 159's analytic inputs; Leng–Sah–Sawhney and Leng](papers/159-szemeredi-exponents/#depends-on) |
| [172](papers/172-euclidean-ramsey/) · [PDF](papers/172-euclidean-ramsey/algebraic_spherical_configurations.pdf) | A tensor criterion characterizing Euclidean Ramsey configurations | Every finite spherical configuration with real algebraic coordinates is Euclidean Ramsey | OpenAI 172, Theorem 1.1 |

Here $`r_k(N)`$ is the largest size of a subset of $`\{1,\ldots,N\}`$ with no nonconstant $`k`$-term arithmetic progression, and $`a`$ is admissible if it is neither $`-1`$ nor a square. TeX sources and precise statements are in each family folder.

## Documentation

- [Pinned upstream references](docs/SOURCES.md)
- [Validation record](docs/VALIDATION.md) and [file hashes](docs/files.json)
- [AI disclosure and licensing](NOTICE.md)

## Reproduction

With Python 3.10+ and TeX Live or MiKTeX, run from the repository root:

~~~sh
python scripts/build.py            # all families, or e.g. build.py 029 159
python scripts/check_certificates.py
~~~

Builds go to `build/`, using `pdflatex` with shell escape disabled. The certificate check verifies the numerical endpoint in the Hecke paper by exact rational arithmetic. Neither step certifies the proofs or their external inputs.
