# Iterative Binary Search
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0  # Count steps for performance evaluation

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid, steps
        # Target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        # Target is larger, ignore left half
        else:
            low = mid + 1

    return -1, steps  # Target not found

# Recursive Binary Search
def binary_search_recursive(arr, low, high, target, steps=0):
    if low > high:
        return -1, steps  # Target not found
    
    steps += 1
    mid = (low + high) // 2
    
    # Target found
    if arr[mid] == target:
        return mid, steps
    # Target is smaller, search in the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target, steps)
    # Target is larger, search in the right half
    else:
        return binary_search_recursive(arr, mid + 1, high, target, steps)





def get_input():
    # Input a list of numbers from the user
    user_list = input("Enter a list of numbers separated by spaces: \n").split()
    arr = [int(num) for num in user_list]
    
    # Input the target number to search
    target = int(input("Enter the number you want to search for: \n"))
    
    return arr, target

def sort_array(arr):
    # Sorting the array before binary search
    arr.sort()
    print(f"Sorted array: {arr}")
    return arr
