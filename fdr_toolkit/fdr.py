import numpy as np

"""
The fdr for the three methods to consider in this work

More details to be added later in due course.
"""

def bonferroni(p_values, alpha=0.05):
    p_values = np.array(p_values)
    m = len(p_values)

    threshold = alpha / m
    rejected = p_values <= threshold

    adjusted = np.minimum(p_values * m, 1.0)

    return {
        "p_values": p_values,
        "adjusted_p_values": adjusted,
        "rejected": rejected
    }
