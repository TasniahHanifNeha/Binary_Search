#------------Binary Search - Using Recurtion (INPUT)-----------------
print("")

def BinarySearch2(array2, low2, high2, search_item2):
    while low2 <= high2:
        mid2 = (low2 + high2) // 2

        if array2[mid2] == search_item2:
            return mid2

        elif array2[mid2] < search_item2:
            low2 = mid2 + 1
        else:
            high2 = mid2 - 1
    return -1


arr =  [int(item) for item in input("Enter the list items : "). split()]
array2 = sorted(arr)

search_item2 = int(input("Enter searching item : "))

result2 = BinarySearch2(array2, 0, len(array2)-1, search_item2)

print("\nSorted list :", array2)

if result2 == -1:
    print ("Element is not present in array")
else:
    print ("Element is present at index", result2)


print("")

