print("")

#----------Iterative Binary Search----------------

def binary_search(arr, s):
    low = 0
    high = len(arr) - 1

 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < s:
            low = mid + 1

        elif arr[mid] > s:
            high = mid - 1
 
        else:
            return mid #present in mid
 
    return -1
 
arr = sorted([ 2, 3, 4, 10, 40 ])
s = 10
 
result = binary_search(arr, s)

print("Sorted list :", arr)
if result != -1:
    print(s, "element is present at index", result)
else:
    print("Element is not present in array")


print("")
