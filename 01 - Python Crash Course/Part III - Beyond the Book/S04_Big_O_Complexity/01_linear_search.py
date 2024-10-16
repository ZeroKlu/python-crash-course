from common_functions import file_to_list, efficiency_report
from random import randint
from sm_utils import timer

# Pseudocode Algorithm:
# ----------------------------------------------
# For i from 0 to n-1
#     If the element at location i is the target
#         Quit (Return the index)
# If target element not found
#     Quit (Return failure state)
# ----------------------------------------------

folder = "data"
file_name = "unordered_integers.txt"

@timer
def linear_search(array: list[int], target: int) -> tuple[int, int]:
    """Find the index where the target value is stored"""
    count = 0
    for i in range(len(array)):
        count += 1
        if array[i] == target:
            return (i, count)
    return (-1, count)

def main() -> None:
    numbers = file_to_list(file_name, folder)
    seek = randint(min(numbers), max(numbers))
    result = linear_search(numbers, seek)
    if result[0] < 0:
        print(f"\nDid not find value: {seek}")
        exit()
    print(f"\nIndex of target [{seek}]: i = [{result[0]}]")
    efficiency_report("Linear Search", len(numbers), result[1])

if __name__ == "__main__":
    main()
