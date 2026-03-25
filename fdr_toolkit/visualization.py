import numpy as np
import matplotlib.pyplot as plt


def plot_bh(p_values, alpha=0.05):
    p_values = np.array(p_values)
    m = len(p_values)

    sorted_pvals = np.sort(p_values)
    ranks = np.arange(1, m + 1)
    bh_line = (ranks / m) * alpha

    plt.scatter(ranks, sorted_pvals)
    plt.plot(ranks, bh_line)

    plt.xlabel("Rank (k)")
    plt.ylabel("p-value")
    plt.title("Benjamini-Hochberg Procedure")

    plt.show()
