# Validation record

Checked on **8 October 2026**. The PDFs from TeX sources were last built with pdfTeX **1.40.25 / TeX Live 2023** on Linux.

## LaTeX compilation and layout

Each available TeX target passes three `pdflatex` runs with shell escape disabled. Final logs contain no unresolved references or duplicate labels.

| Family | Target | Result |
| --- | --- | --- |
| 029 | `artin_positive_density.tex` | Pass |
| 029 | `hecke_zero_free_strip.tex` | Pass |
| 029 | `hecke_seven_eighths_all_characters.tex` | Pass |
| 030 | `modularity_cm_totally_real.tex` | Pass |
| 159 | `math159_one_level_bound.tex` | Pass |
| 172 | `algebraic_spherical_configurations.tex` | Pass |

The rebuilt PDFs were compared with the previous builds: page counts and text agree except for the title block. The 017 PDF has no TeX source; its first page was edited directly, leaving the mathematical text unchanged. Compiler versions and PDF metadata can affect byte-for-byte reproduction. Build output goes to `build/`.

## Finite computation check

The Hecke endpoint certificate passes its assertions and matches the recorded output, ignoring line-ending differences and trailing whitespace. The machine-readable result is in [certificate-validation.json](certificate-validation.json). The runner writes output to `build/certificates/` and `build/certificate-summary.json`.

The certificate uses exact rational arithmetic to verify

```math
0.096906264531643757<\Delta_\#<0.096906264531643758.
```

It checks the numerical enclosure. The mathematical statement and analytic inputs are described in the [029 README](../papers/029-artin-primitive-roots/).

## File integrity

[files.json](files.json) records sizes and SHA-256 hashes for the manuscript and certificate files.

Compilation and finite computations do not certify the complete mathematical proofs or their external inputs. Each family README states its dependencies. No Lean verification is asserted for this collection.
