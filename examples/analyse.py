# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:34:57 2026

@author: odunla
"""

import pandas as pd
import numpy as np

from multiple_testing_toolkit.fdr_toolkit import benjamini_hochberg

from multiple_testing_toolkit.fdr_toolkit import bonferroni

pvals = [0.001, 0.01, 0.015, 0.03, 0.04, 0.20]

bh_results = benjamini_hochberg(pvals)
bonf_results = bonferroni(pvals)

print(bh_results)
print(bonf_results)

