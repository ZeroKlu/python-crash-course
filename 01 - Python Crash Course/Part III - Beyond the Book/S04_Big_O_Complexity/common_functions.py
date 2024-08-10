from relative_paths import get_path
from pathlib import Path
from math import log2, ceil

def file_to_list(file_name: str, folder: str=None) -> list[int]:
    """Read a space-delimited file into a list of integers"""
    numbers = []
    path = Path(get_path(file_name, folder))
    for line in path.read_text().splitlines():
        numbers += [int(n) for n in line.split()]
    return numbers

def list_to_file(array: list[int], file_name: str, folder: str=None) -> None:
    """Write a list of integers a space-delimited file"""
    path = Path(get_path(file_name, folder))
    path.write_text(" ".join(str(n) for n in array))

def complexities(n: int) -> dict[dict[str, any]]:
    """Calculate predicted operations by complexity"""
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
            "big_o": "n log n",
            "count": int(ceil(n * log2(n)))
        },
        "n": {
            "name": "linear",
            "big_o": "n",
            "count": n
        },
        "log_n": {
            "name": "logarithmic",
            "big_o": "log n",
            "count": int(ceil(log2(n)))
        },
        "const": {
            "name": "constant",
            "big_o": "1",
            "count": 1
        }
    }

def efficiency_report(algorithm: str, size: int, count: int) -> None:
    """Print out a report of the Big-O efficiency of the algorithm"""
    print(f"\n{algorithm} performed {count:,}", end=" ")

    if "search" in algorithm.lower():
        print(f"comparisons to search {size:,} numbers.\n")
    else:
        print(f"operations to sort {size:,} numbers\n")

    big_o = complexities(size)

    o = big_o["const"]
    if count > big_o["n_squared"]["count"] * 2:
        o = big_o["exp"]
    elif count > big_o["n_log_n"]["count"] * 2:
        o = big_o["n_squared"]
    elif count > big_o["n"]["count"] * 2:
        o = big_o["n_log_n"]
    elif count > big_o["log_n"]["count"] * 2:
        o = big_o["n"]
    elif count > 2:
        o = big_o["log_n"]
        
    print(f"Computed complexity: O({o['big_o']}) - {o['name']}\n")
    print("Approximate values for reference:")
    print(" · n!       = Value omitted - too large to calculate!")
    print(" · 2ⁿ       = Value omitted - too large to calculate!")
    print(f" · n²       = {big_o['n_squared']['count']:,}")
    print(f" · n log(n) = {big_o['n_log_n']['count']:,}")
    print(f" · n        = {big_o['n']['count']:,}")
    print(f" · log(n)   = {big_o['log_n']['count']:,}\n")
