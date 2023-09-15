from random import randint
import math
from typing import List

class SortMethods:
    """Class to define a set of sorting algorithms"""

    def __init__(self, num_elements = 5000, min = -5000, max = 5000):
        """Initialize the global variables"""
        self.min = min
        self.max = max
        self.last_sort = ""
        self.unsorted = []
        self.sorted = []
        # Populate the unsorted array
        for i in range(0, num_elements):
            self.unsorted.append(randint(min, max))

    def bubble_sort(self, array = None):
        """Iterate repeatedly over list and swap pairs so higher elements move to end of list"""
        # Order n^2
        if array == None: array = self.unsorted[:]
        swapped = False
        # In our outer loop, we iterate across the entire list
        for i in range(len(array) - 1, 0, -1):
            # Within each iteration, we compare against all earlier cells in the list
            for j in range(i):
                if array[j] > array[j + 1]:
                    # When an earlier cell is less than its adjacent cell, swap their values
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped= True
            if swapped:
                # Move on to the next item
                swapped=False
            else:
                # We got to the end without more swaps
                break
        self.last_sort = "bubble"
        return array

    def selection_sort(self, array = None):
        """Split array in two parts and continuously move smallest element from unsorted to sorted segment"""
        # Order n^2
        if array == None: array = self.unsorted[:]
        # Iterate across entire unsorted list
        for i in range(len(array) - 1):
            min_index = i
            # Iterate across remainder of array
            for index in range(i + 1, len(array)):
                if array[index] < array[min_index]:
                    # # Find nest element to sort
                    min_index = index
            # Swap values
            array[i], array[min_index] = array[min_index], array[i]
        self.last_sort = "selection"
        return array

    def insertion_sort(self, array = None):
        """Split array in two parts and continuously move each element to its position in sorted segment"""
        # Order n^2
        if array == None: array = self.unsorted[:]
        # Iterate across entire unsorted list (except first element)
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while array[j] > key and j >= 0:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        self.last_sort = "insertion"
        return array

    def shell_sort(self, array = None):
        """Optimize insertion sort by repeatedly decreasing insertion interval"""
        # Order n^2
        if array == None: array = self.unsorted[:]
        n = len(array)
        k = int(math.log2(n))
        # Here, we are setting the initial interval
        interval = 2 ** k - 1
        while interval > 0:
            # Run an insertion sort within the interval
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                array[j] = temp
            k -= 1
            # Set the next smaller interval
            interval = 2 ** k - 1
        self.last_sort = "shell"
        return array

    def make_heap(self, array, n, i):
        """Create the heap structure for heap sorting"""
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r
        
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.make_heap(array, n, largest)

    def heap_sort(self, array = None):
        """Use heap structure to efficiently find largest element"""
        # Order n*log(n)
        if array == None: array = self.unsorted[:]
        n = len(array)
        for i in range(n // 2, -1, -1):
            self.make_heap(array, n, i)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.make_heap(array, i, 0)
        self.last_sort = "heap"
        return array

    def merge_lists(self, lst1, lst2):
        """Merge two lists used in merge sort"""
        lst = []
        i = 0
        j = 0
        while(i <= len(lst1) - 1 and j <= len(lst2) - 1):
            if lst1[i] < lst2[j]:
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1
        if i > len(lst1)-1:
            while(j <= len(lst2) - 1):
                lst.append(lst2[j])
                j += 1
        else:
            while(i <= len(lst1) - 1):
                lst.append(lst1[i])
                i += 1
        return lst

    def merge_sort(self, array = None):
        """???"""
        # Order n*log(n)
        if array == None: array = self.unsorted[:]
        if len(array) == 1:
            return array
        mid = (len(array) - 1) // 2
        lst1 = self.merge_sort(array[:mid + 1])
        lst2 = self.merge_sort(array[mid + 1:])
        result = self.merge_lists(lst1, lst2)
        self.last_sort = "merge"
        return result

    def quick_sort(self, array = None):
        """Continuously split the list around a pivot point"""
        # Order n*log(n)
        if array == None: array = self.unsorted[:]
        if len(array) > 1:
            pivot = array.pop()
            grtr_lst, equal_lst, smlr_lst = [], [pivot], []
            for item in array:
                if item == pivot:
                    equal_lst.append(item)
                elif item > pivot:
                    grtr_lst.append(item)
                else:
                    smlr_lst.append(item)
            return (self.quick_sort(smlr_lst) + equal_lst + self.quick_sort(grtr_lst))
        else:
            self.last_sort = "quick"
            return array

    def default_sort(self, array = None):
        if array == None: array = self.unsorted[:]
        self.last_sort = "default"
        return sorted(array)
