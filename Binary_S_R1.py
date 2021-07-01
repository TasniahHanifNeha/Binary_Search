print("")

#-------------Binary Search - Using Recurtion------------------

def BinarySearch(array, low, high, search_item):
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == search_item:
            return mid

        elif array[mid] < search_item:
            low = mid + 1

        else:
            high = mid - 1 
        
    return -1


array =  sorted([12, 28, 25, 10, 40, 55, 60])
search_item = 25
result = BinarySearch(array, 0, len(array)-1, search_item)

print("Sorted array :", array)
if result == -1:
    print ("Element is not present in array")
else:
    print ("Element is present at index", result)



print("")


