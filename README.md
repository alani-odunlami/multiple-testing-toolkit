# multiple-testing-toolkit
This repo is simple implementation of bonferroni and Benjamini-Hochberg Family-wise error rate (FWER) and False discovery rate (FDR)

A Python toolkit for correcting multiple hypothesis testing problems using statistically rigorous methods like Benjamini–Hochberg (FDR) and Bonferroni correction.


## 📌 The Problem
When testing multiple hypotheses, the chance of false positives increases rapidly:

- Testing 100 hypotheses at α = 0.05

- 👉 Expected false positives = 5

Even worse, the probability of at least one false positive becomes very high.

This leads to misleading conclusions in:

- A/B testing
- Feature selection
- Experimentation platforms


## 💡 The Solution

This toolkit implements:

✅ **Benjamini–Hochberg (FDR)**
- Controls the False Discovery Rate
- More powerful (finds more true signals)
- Ideal for data science & experimentation

✅ **Bonferroni Correction**
- Controls Family-Wise Error Rate (FWER)
- Very strict (minimises false positives)
- Best for high-risk decisions


⚡ Quick Start
from fdr_toolkit.fdr import benjamini_hochberg

p_vals = [0.12, 0.03, 0.001, 0.20, 0.04,
          0.002, 0.15, 0.05, 0.30, 0.01]

results = benjamini_hochberg(p_vals, alpha=0.05)

print(results)
