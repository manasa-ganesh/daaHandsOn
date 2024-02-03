b. Argue Selection Sort Correctness

Selection sort is a simple and straightforward sorting algorithm, but it may not be the most efficient choice for large datasets. Let's discuss its correctness and some aspects of its performance:

Correctness:

The basic idea behind selection sort is to divide the input into a sorted and an unsorted region. During each iteration of the selection sort algorithm, an exhaustive search is conducted within the unsorted region of the array to ascertain the minimum element. Following the identification of this minimal value, a strategic exchange is orchestrated, relocating the selected minimum to the foremost position within the unsorted region. This iterative procedure persists until the entirety of the array is meticulously arranged in ascending order, thus achieving a sorted state. The fundamental principle lies in the sequential curation of the minimum elements from the unsorted sector, systematically positioning them at the outset of the unsorted domain until the entire array attains a discernibly ordered configuration.

The correctness of selection sort can be demonstrated by the loop invariant. At the beginning of each iteration, the smallest unsorted element is selected and placed in its correct position. This process repeats until the entire array is sorted. The algorithm is guaranteed to terminate and produce a correctly sorted array.

The time complexity of selection sort is O(n^2), where n is the number of elements in the array. This is because, for each element in the array, the algorithm has to find the minimum element in the unsorted region, which involves comparing n elements in the worst case.

While selection sort is correct, it is not the most efficient sorting algorithm for large datasets due to its time complexity. Its quadratic time complexity makes it less suitable for sorting large datasets compared to more advanced algorithms like merge sort or quicksort, which have average-case time complexities of O(n log n).


c. System Specifications:

System information:
CPU: Windows 10.0.22621
Total RAM: 16805036032 bytes
System: Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

Storage information:
C:\ - Total: 368129863680 bytes, Free: 243057664000 bytes
D:\ - Total: 318787022848 bytes, Free: 257257058304 bytes
E:\ - Total: 335544315904 bytes, Free: 316200505344 bytes
G:\ - Total: 16106127360 bytes, Free: 661610496 bytes