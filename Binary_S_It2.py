print("")

#----------Iterative Binary Search (INPUT)----------------


def BinarySearch(array,search_item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == search_item:
            return mid

        elif array[mid] < search_item:
            low = mid + 1

        else:
            high = mid - 1
    return -1

array = sorted([int(item) for item in input("Enter the list items : "). split()])
search_item = int(input("Enter searching item : "))
 
result = BinarySearch(array, search_item)

print("Sorted list :", array)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")



print("")


