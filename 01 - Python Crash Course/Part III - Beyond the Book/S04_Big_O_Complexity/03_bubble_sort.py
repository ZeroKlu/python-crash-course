from common_functions import file_to_list, efficiency_report, list_to_file
from sm_utils import timer

# Pseudocode Algorithm:
# --------------------------------------------------------------
# Repeat n-1 times
#     For i from 0 to n-2
#         If list[i] and list[i+1] are out of order
#             Swap them
#     If no swaps occurred
#         Quit
# --------------------------------------------------------------

folder = "data"
input_file_name = "unordered_integers.txt"
output_file_name = "sorted_integers.txt"

@timer
def bubble_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the bubble sort algorithm"""
    count = 0

    for _ in range(len(array)):
        swap = False
        for i in range(len(array) - 1):
            count += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        if not swap:
            break
    
    return (array, count)

def main() -> None:
    numbers = file_to_list(input_file_name, folder)
    result = bubble_sort(numbers)
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Bubble Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
