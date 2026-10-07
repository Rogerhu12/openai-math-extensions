# 172 — Algebraic spherical configurations

**Research draft** · [PDF](algebraic_spherical_configurations.pdf) · [TeX](algebraic_spherical_configurations.tex)

[OpenAI 172](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf#page=2) characterizes Euclidean Ramsey configurations by a tensor criterion over $`F\otimes_{\mathbb Q}F`$, where $`F`$ is the coordinate field. This two-page note shows that the criterion holds whenever the configuration is spherical and its coordinates are real algebraic numbers.

**Theorem.** Assuming OpenAI 172, Theorem 1.1, every finite nonempty spherical configuration with real algebraic coordinates is Euclidean Ramsey.

Here Ramsey means that, for each finite number of colors, some finite-dimensional Euclidean space forces a monochromatic congruent copy at the original scale under every coloring; no measurability is assumed. The proof uses the separability idempotent of the coordinate number field and a reduction to the affine span. In particular, the seven-point family

```math
P_t=\{(0,0)\}\cup\{(j,\pm\sqrt{j(2t-j)}):j=1,3,4\}
```

is Ramsey for every real algebraic $`t>2`$.

**Depends on:** OpenAI 172, Theorem 1.1, and the results used in its proof.
