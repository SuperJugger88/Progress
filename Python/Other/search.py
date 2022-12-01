def linear(x):
    arr = list(range(1, 1001))
    try:
        return next((i, 'ID: ' + str(arr.index(i))) for i in arr if i == x)
    except StopIteration:
        return 'Not found'

print(linear(57))

def binary(y):
    arr = list(range(1, 1001))
    left, right = arr[0] , len(arr)-1
    mid = len(arr)//2

    while arr[mid] != y  and left <= right:
        if y > arr[mid]:
            left = mid +1
        else:
            right = mid -1
        mid = (left+right)//2

    return 'Not found' if left > right else (arr[mid], 'ID: ' + str(mid))

print(binary(57))

