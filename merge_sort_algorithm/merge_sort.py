def merge_sort(arr):
    # If the array is more than one element, we need to split and merge
    if len(arr) > 1:
        # Find the midpoint of the array
        mid = len(arr)//2

        # Splitting the array elements into 2 halves
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Sorting the first half
        merge_sort(left_arr)
        # Sorting the second half
        merge_sort(right_arr)

        # Initializing pointers for left_arr (i), right_arr (j), and the main array (k)
        i = j = k = 0

        # Merging the arrays back together
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Checking if any element was left in the left half
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Checking if any element was left in the right half
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    # Once all parts are merged back, the array is sorted
    return arr

# Example usage
test_arr = [50, 5, 87, 23, 97, 13, 8, 35, 86]
print(merge_sort(test_arr))
