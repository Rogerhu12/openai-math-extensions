# OpenAI/math 结果的推广

[English](README.md)

AI 辅助研究草稿，详见 [AI 披露](NOTICE.md)。本文集独立于 OpenAI/math。

下列结论均以最后一栏所列输入为条件，均未经同行评审或形式化验证。

## 论文目录

| 编号 | OpenAI 原结果 | 本文集的推广 | 依赖 |
| --- | --- | --- | --- |
| [017](papers/017-rational-logarithms/) · [PDF](papers/017-rational-logarithms/log-rational-irrationality-proof.pdf) | $`\mu(\pi)=2`$ | 对每个有理数 $`a>0`$，$`a\ne1`$，有 $`\mu(\log a)=2`$ | OpenAI 017 的 Lemma 2.2 |
| [029](papers/029-artin-primitive-roots/) · [Artin PDF](papers/029-artin-primitive-roots/artin_positive_density.pdf) · [Hecke $`7/8`$ PDF](papers/029-artin-primitive-roots/hecke_seven_eighths_all_characters.pdf) · [Hecke $`25/258`$ PDF](papers/029-artin-primitive-roots/hecke_zero_free_strip.pdf) | 对每个容许的 $`a`$，$`(x,2x]`$ 中以 $`a`$ 为原根的素数 $`\gg_a x/(\log x)^2`$；含 $`\mu_{12}`$ 的分圆域上 Hecke 无零带宽度 $`10^{-6}`$ | $`\gg_a x/\log x`$，即正下相对密度。任意数域上的任意酉 Hecke 特征（有限阶或无穷阶）满足 $`L(s,\psi)\ne0`$（$`\Re s>7/8`$）；另一条独立路线对有限阶特征给出宽度 $`25/258`$ | [$`7/8`$：OpenAI 003 与 029 的构造推广到一般域；$`25/258`$：OpenAI 029 与 de Faveri 的大筛；Artin：素数前驱估计](papers/029-artin-primitive-roots/#mathematical-dependencies) |
| [030](papers/030-modularity/) · [PDF](papers/030-modularity/modularity_cm_totally_real.pdf) | 虚二次域上的椭圆曲线都模 | 任意全实域上、以及任意 $`\zeta_5\notin K`$ 的 CM 域 $`K`$ 上的椭圆曲线都模；含 $`\zeta_5`$ 的 CM 域在假设 Proposition 10.1 时同样成立 | [OpenAI 030 的几何与局部输入](papers/030-modularity/#dependencies)；含 $`\zeta_5`$ 的 CM 域还需 Proposition 10.1 中拟议的提升论证 |
| [159](papers/159-szemeredi-exponents/) · [PDF](papers/159-szemeredi-exponents/math159_one_level_bound.pdf) | 对某个 $`\varepsilon_k>0`$ 有 $`r_k(N)\le K_kN\exp[-c_k(\log N)^{\varepsilon_k}]`$，未给出对 $`k`$ 的依赖 | 同一界，$`\varepsilon_k=\exp(-k^C)`$，$`C`$ 为绝对常数 | [OpenAI 159 的解析输入；Leng–Sah–Sawhney 与 Leng](papers/159-szemeredi-exponents/#depends-on) |
| [172](papers/172-euclidean-ramsey/) · [PDF](papers/172-euclidean-ramsey/algebraic_spherical_configurations.pdf) | 刻画 Euclidean Ramsey 构型的张量判据 | 所有坐标为实代数数的有限球面构型都是 Euclidean Ramsey 的 | OpenAI 172 的 Theorem 1.1 |

这里 $`r_k(N)`$ 是 $`\{1,\ldots,N\}`$ 中不含非平凡 $`k`$ 项等差数列的子集的最大大小；$`a`$ 容许指 $`a`$ 既不是 $`-1`$ 也不是平方数。TeX 源文件与精确陈述见各编号目录。

## 文档

- [固定版本的上游参考](docs/SOURCES.md)
- [验证记录](docs/VALIDATION.md)与[文件哈希](docs/files.json)
- [AI 披露与许可](NOTICE.md)

## 复现方法

需要 Python 3.10+ 与 TeX Live 或 MiKTeX。在仓库根目录运行：

~~~sh
python scripts/build.py            # 编译全部，或如 build.py 029 159
python scripts/check_certificates.py
~~~

编译结果写入 `build/`，使用禁用 shell escape 的 `pdflatex`。证书检查以精确有理数运算验证 Hecke 论文中的数值端点。两者都不构成对证明或其外部输入的认证。
