from numpy import ndarray, long
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def binomial_kde(bin: ndarray[long]) -> None:
    """Plot a binomial distribution's KDE curve"""
    sns.kdeplot(bin, fill=True, color="blue")
    plt.show()

def binomial_hist(bin: ndarray[long]) -> None:
    """Plot a binomial distribution's histogram"""
    sns.histplot(bin)
    plt.show()

def binomial_vs_normal(bin: ndarray[long], norm: ndarray[long]) -> None:
    """Plot a binomial distribution compared with a normal distribution"""
    sns.kdeplot(bin, fill=True, color="blue", label="Binomial")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    rng = random.default_rng()
    bin = rng.binomial(n=10, p=0.5, size=1000)
    binomial_kde(bin)
    binomial_hist(bin)
    norm = rng.normal(loc=5, scale=1, size=1000)
    binomial_vs_normal(bin, norm)

if __name__ == "__main__":
    main()
