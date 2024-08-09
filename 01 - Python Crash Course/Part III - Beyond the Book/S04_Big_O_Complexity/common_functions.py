from relative_paths import get_path
from pathlib import Path
from math import log2

def file_to_list(file_name: str, folder: str=None) -> list[int]:
    """Read a space-delimited file into a list of integers"""
    numbers = []
    path = Path(get_path(file_name, folder))
    for line in path.read_text().splitlines():
        numbers += [int(n) for n in line.split()]
    return numbers

def complexities(n: int) -> dict[dict[str, any]]:
    """Calculate predicted operations by complexity"""
    log = int(log2(n))
    return {
        "exp": {
            "name": "exponential",
            "big_o": "2ⁿ",
            "count": 0
        },
        "n_squared": {
            "name": "quadratic (polynomial)",
            "big_o": "n²",
            "count": n ** 2
        },
        "n_log_n": {
            "name": "loglinear",
            "big_o": "n log(n)",
            "count": n * log
        },
        "n": {
            "name": "linear",
            "big_o": "n",
            "count": n
        },
        "log_n": {
            "name": "logarithmic",
            "big_o": "log(n)",
            "count": log
        },
        "const": {
            "name": "constant",
            "big_o": "1",
            "count": 1
        }
    }

def efficiency_report(algorithm: str, size: int, count: int) -> None:
    """Print out a report of the Big-O efficiency of the algorithm"""
    print(f"{algorithm} performed {count:,}", end=" ")
    print(f"comparisons to search {size:,} numbers.\n")

    big_o = complexities(size)

    o = "const"
    if count > big_o["n_squared"]["count"]:
        o = big_o["exp"]
    elif count > big_o["n_log_n"]["count"]:
        o = big_o["n_squared"]
    elif count > big_o["n"]["count"]:
        o = big_o["n_log_n"]
    elif count > big_o["log_n"]["count"]:
        o = big_o["n"]
    elif count > 1:
        o = big_o["log_n"]

    print(f"Computed complexity: O({o['big_o']}) - {o['name']}\n")
    print("Approximate values for reference:")
    print(" · n!       = Value omitted - too large to calculate!")
    print(" · 2ⁿ       = Value omitted - too large to calculate!")
    print(f" · n²       = {big_o['n_squared']['count']:,}")
    print(f" · n log(n) = {big_o['n_log_n']['count']:,}")
    print(f" · n        = {big_o['n']['count']:,}")
    print(f" · log(n)   = {big_o['log_n']['count']:,}\n")
