from sort_methods import SortMethods
import time

def pause():
    input("Press <ENTER> to continue:\n> ")

def main():
    sorter = SortMethods()
    # sorter = SortMethods(10_000, -5_000, 5_000)

    do_sort(sorter, sorter.bubble_sort)
    pause()

    do_sort(sorter, sorter.selection_sort)
    pause()

    do_sort(sorter, sorter.insertion_sort)
    pause()

    do_sort(sorter, sorter.shell_sort)
    pause()

    do_sort(sorter, sorter.heap_sort)
    pause()

    do_sort(sorter, sorter.merge_sort)
    pause()

    do_sort(sorter, sorter.quick_sort)
    pause()

    do_sort(sorter, sorter.default_sort)

def do_sort(sorter, sort_method, print_sorted = False):
    """Perform the specified sorting algorithm"""
    start_time = time.time()
    sorter.sorted = sort_method()
    duration = time.time() - start_time
    if print_sorted:
        for num in sorter.sorted:
            print(num)
    print(f"\n{sorter.last_sort.title()} sort completed in {duration} seconds.")
    print(f"Unsorted: [{sorter.unsorted[0]} - {sorter.unsorted[-1]}]")
    print(f"Sorted:   [{sorter.sorted[0]} - {sorter.sorted[-1]}]\n")

if __name__ == "__main__":
    main()
