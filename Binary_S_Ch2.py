print("")

#-----------Binary Search - Character(INPUT)-----------

def find(array, search_item):
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


array = sorted([str(item) for item in input("Enter the list items : "). split()])
search_item = str(input("Enter searching item : "))

result = find(array, search_item)
print(sorted(array))

print("Sorted array :", array)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")




print("")
