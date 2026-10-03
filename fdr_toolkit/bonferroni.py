import numpy as np
import pandas as pd


def bonferroni(p_values, alpha=0.05, return_df=True):
    """
    Perform Bonferroni FWER correction.

    Parameters
    ----------
    p_values : array-like
        List or array of p-values.
    alpha : float, optional (default=0.05)
        Desired family-wise error rate.
    return_df : bool, optional (default=True)
        If True, returns results as a pandas DataFrame.

    Returns
    -------
    results : pd.DataFrame or dict
        Contains:
        - original p-values
        - adjusted p-values
        - rejected (True/False)
    """

    p_values = np.array(p_values)
    m = len(p_values)

    # Bonferroni-adjusted significance threshold
    threshold = alpha / m

    # Rejection decision
    rejected = p_values <= threshold

    # Adjusted p-values
    adjusted_pvals = np.minimum(p_values * m, 1.0)

    if return_df:
        return pd.DataFrame({
            "p_value": p_values,
            "adjusted_p_value": adjusted_pvals,
            "p_threshold": threshold,
            "rejected": rejected
        })

    return {
        "p_values": p_values,
        "adjusted_p_values": adjusted_pvals,
        "p_threshold": threshold,
        "rejected": rejected
    }


pvals = [0.001, 0.01, 0.03, 0.04, 0.20]

print(bonferroni(pvals))
