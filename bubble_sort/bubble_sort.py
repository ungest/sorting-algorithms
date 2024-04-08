def bubble_sort(item_list):
    # The outer loop runs once for each element in the list
    for a in range(len(item_list)):
        # The inner loop compares adjacent elements and swaps them if they are in the wrong order
        for i in range(len(item_list) -1):
            # Compare each pair of adjacent items, swap them if they are in the wrong order
            if item_list[i] > item_list[i + 1]:
                # Swap operation using tuple unpacking
                item_list[i], item_list[i + 1] = item_list[i + 1], item_list[i]
    # Once all elements have been passed through and no swaps are needed, the list is sorted
    return item_list

# Example usage
item_list = [4, 1, 3, 2]
print(bubble_sort(item_list))