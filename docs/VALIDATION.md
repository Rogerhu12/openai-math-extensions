# Validation record

Checked on **8 October 2026**. All available TeX sources were compiled with pdfTeX **1.40.26 / TeX Live 2024** on Windows. The stored Hecke PDF uses this build; the other stored PDFs from TeX sources were built with pdfTeX **1.40.25 / TeX Live 2023** on Linux.

## LaTeX compilation and layout

Each available TeX target passes three `pdflatex` runs with shell escape disabled. Final logs contain no unresolved references or duplicate labels.

| Family | Target | Result |
| --- | --- | --- |
| 029 | `artin_positive_density.tex` | Pass |
| 029 | `hecke_zero_free_strip.tex` | Pass |
| 030 | `modularity_cm_totally_real.tex` | Pass |
| 172 | `algebraic_spherical_configurations.tex` | Pass |

The compiled PDFs were compared with the stored PDFs: page counts and extracted text agree. The Hecke PDF was rendered for layout review after correcting the conjugate character in its reflected denominator and the accompanying explanation. Compiler versions and PDF metadata can affect byte-for-byte reproduction. Build output goes to `build/`.

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
