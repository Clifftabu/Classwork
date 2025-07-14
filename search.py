arr = [11,22,33,44,55,66,77,88,99]
key = 77
startIndex = arr[0]
endIndex = len(arr)-1

found = False


while startIndex <=endIndex:
    mid = (startIndex + endIndex)//2
    if arr[mid] ==key:
        print("found Element at pos "mid)
        found = True
    elif key < arr[mid]:
        endIndex = mid -1
    elif key < arr[mid]:
        startIndex = mid + 1
    if not found:
        print("Nothing has been found")


