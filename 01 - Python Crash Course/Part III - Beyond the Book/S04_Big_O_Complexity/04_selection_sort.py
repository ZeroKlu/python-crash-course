from common_functions import file_to_list, efficiency_report, list_to_file
from sm_utils import timer

# Pseudocode Algorithm:
# --------------------------------------------------------------
# For i from 0 to n-1
#     Find the smallest element between array[i] and array[n-1].
#     Swap the smallest element with array[i]
# --------------------------------------------------------------

folder = "data"
input_file_name = "unordered_integers.txt"
output_file_name = "sorted_integers.txt"

@timer
def selection_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the selection sort algorithm"""
    count = 0
    for i in range(len(array)):
        least = array[i]
        p = i + 1
        for j in range(p, len(array)):
            count += 1
            if array[j] < least:
                p = j
                least = array[j]
        if least < array[i]:
            array[i], array[p] = array[p], array[i]
    return (array, count)

def main() -> None:
    numbers = file_to_list(input_file_name, folder)
    result = selection_sort(numbers)
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Selection Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
