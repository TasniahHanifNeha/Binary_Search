

print("")
#-----------Binary Search - Character-----------

def find(array, search_item):
    low = 0
    high = len(array) - 1
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if array[mid] < search_item:
            low = mid + 1

        elif array[mid] > search_item:
            high = mid - 1
 
        else:
            return mid #present in mid
    return -1
 
array = sorted(["Bin", "Lee", "Seung", "Suzy", "Eun", "Shin"])
search_item = "Shin"
result = find(array, search_item)

print("Sorted array :", array)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")




print("")