import numpy as np
import pandas as pd


def benjamini_hochberg(p_values, alpha=0.05, return_df=True):
    """
    Perform Benjamini-Hochberg FDR correction.

    Parameters
    ----------
    p_values : array-like
        List or array of p-values.
    alpha : float, optional (default=0.05)
        Desired false discovery rate.
    return_df : bool, optional (default=True)
        If True, returns results as a pandas DataFrame.

    Returns
    -------
    results : pd.DataFrame or dict
        Contains:
        - original p-values
        - sorted p-values
        - BH threshold
        - rejected (True/False)
        - adjusted p-values
    """

    p_values = np.array(p_values)
    m = len(p_values)

    # Sort p-values and keep original indices
    sorted_indices = np.argsort(p_values)
    sorted_pvals = p_values[sorted_indices]

    # Compute BH thresholds
    ranks = np.arange(1, m + 1)
    bh_thresholds = (ranks / m) * alpha

    # Determine rejection
    below = sorted_pvals <= bh_thresholds
    max_k = np.where(below)[0].max() if np.any(below) else -1

    rejected = np.zeros(m, dtype=bool)
    if max_k >= 0:
        rejected[sorted_indices[:max_k + 1]] = True

    # Compute adjusted p-values (important for reporting)
    adjusted_pvals = np.empty(m)
    adjusted_sorted = (m / ranks) * sorted_pvals
    adjusted_sorted = np.minimum.accumulate(adjusted_sorted[::-1])[::-1]
    adjusted_sorted = np.clip(adjusted_sorted, 0, 1)

    # Reorder to original positions
    adjusted_pvals[sorted_indices] = adjusted_sorted

    if return_df:
        return pd.DataFrame({
            "p_value": p_values,
            "adjusted_p_value": adjusted_pvals,
            "rejected": rejected
        })

    return {
        "p_values": p_values,
        "adjusted_p_values": adjusted_pvals,
        "rejected": rejected
    }
