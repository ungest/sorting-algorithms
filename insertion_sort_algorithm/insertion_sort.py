def insertion_sort(arr):
    # Loop from the second element of the array until the last element
    for i in range(1, len(arr)):
        # This is the element we want to position in its correct place
        j = i
        # Initialize the variable 'j' at the current index. 
        # Move down the array (to the left), comparing each item with the one before it
        while j > 0 and arr[j-1] > arr[j]:
            # Swap elements if the element on the left is larger than the one on the right
            arr[j-1], arr[j] = arr[j], arr[j-1]
            # Move to the next element on the left
            j -= 1
    # Return the sorted array
    return arr

# Example usage of the function
items = [4, 8, 0, 2, 5, 8, 3]
print(insertion_sort(items))
