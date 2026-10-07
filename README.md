# Extensions of results in OpenAI/math

[中文说明](README.zh-CN.md)

AI-assisted research drafts; see [AI disclosure](NOTICE.md). This collection is independent of OpenAI/math.

Every result below is conditional on the inputs in its last column. None has been refereed or formally verified.

## Papers

| Family | OpenAI result | Extension | Depends on |
| --- | --- | --- | --- |
| [017](papers/017-rational-logarithms/) · [PDF](papers/017-rational-logarithms/log-rational-irrationality-proof.pdf) | $`\mu(\pi)=2`$ | $`\mu(\log a)=2`$ for every rational $`a>0`$, $`a\ne1`$ | OpenAI 017, Lemma 2.2 |
| [029](papers/029-artin-primitive-roots/) · [Artin PDF](papers/029-artin-primitive-roots/artin_positive_density.pdf) · [Hecke PDF](papers/029-artin-primitive-roots/hecke_zero_free_strip.pdf) | For each admissible $`a`$, $`\gg_a x/(\log x)^2`$ primitive-root primes in $`(x,2x]`$; Hecke zero-free width $`10^{-6}`$ over cyclotomic fields containing $`\mu_{12}`$ | $`\gg_a x/\log x`$, i.e. positive lower relative density; Hecke zero-free width $`25/258`$ over every number field | [OpenAI 029 and prime-predecessor estimates; de Faveri's large sieve](papers/029-artin-primitive-roots/#mathematical-dependencies) |
| [030](papers/030-modularity/) · [PDF](papers/030-modularity/modularity_cm_totally_real.pdf) | Elliptic curves over imaginary quadratic fields are modular | Elliptic curves over every totally real field, and over every CM field $`K`$ with $`\zeta_5\notin K`$, are modular. Over CM fields containing $`\zeta_5`$, the same holds assuming Proposition 10.1 | [OpenAI 030's geometric and local inputs](papers/030-modularity/#dependencies); for CM fields containing $`\zeta_5`$, also the proposed lifting argument of Proposition 10.1 |
| [172](papers/172-euclidean-ramsey/) · [PDF](papers/172-euclidean-ramsey/algebraic_spherical_configurations.pdf) | A tensor criterion characterizing Euclidean Ramsey configurations | Every finite spherical configuration with real algebraic coordinates is Euclidean Ramsey | OpenAI 172, Theorem 1.1 |

Here $`a`$ is admissible if it is neither $`-1`$ nor a square. TeX sources and precise statements are in each family folder.

## Documentation

- [Pinned upstream references](docs/SOURCES.md)
- [Validation record](docs/VALIDATION.md) and [file hashes](docs/files.json)
- [AI disclosure and licensing](NOTICE.md)

## Reproduction

With Python 3.10+ and TeX Live or MiKTeX, run from the repository root:

~~~sh
python scripts/build.py            # all families, or e.g. build.py 029 030
python scripts/check_certificates.py
~~~

Builds go to `build/`, using `pdflatex` with shell escape disabled. The certificate check verifies the numerical endpoint in the Hecke paper by exact rational arithmetic. Neither step certifies the proofs or their external inputs.
