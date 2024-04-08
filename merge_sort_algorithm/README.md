## Merge Sort Algorithm

### Explanation of the Algorithm:

- **Merge Sort** is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
- The `merge_sort` function first divides the array into two halves until it cannot be divided anymore (i.e., it has only one element), and then it merges the arrays in a sorted manner.

### Computational Complexity:

- **Time Complexity**: The average and worst-case time complexity of Merge Sort is \(O(n \log n)\), where \(n\) is the number of elements in the array.
- **Space Complexity**: Merge Sort requires additional space proportional to the array size for the temporary arrays used during the merge process, giving it a space complexity of \(O(n)\).

### Characteristics:

- **Stable**: Merge Sort is a stable algorithm as it does not change the relative order of elements with equal keys.
- **Not In-Place**: Due to its use of temporary arrays, Merge Sort is not an in-place sorting algorithm.
- **Divide and Conquer**: It utilizes the divide and conquer strategy, dividing the problem into smaller, more manageable problems and then combining the solutions.

This explanation highlights how Merge Sort works, along with its complexity and characteristics, providing a thorough understanding of the algorithm.
