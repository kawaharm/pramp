"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and 
you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 
3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns 
the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can 
be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
Constraints:

[time limit] 5000ms
[input] array.integer arr
[input] integer num
[output] integer
"""


def shifted_arr_search(shiftArr, num):
    '''
    1. Find pivot point
    2. Use binary search on left or right of pivot point:
       - If pivot == 0 (array sorted) or num < start
            binary_search(pivot, end)
       - Else
            binary_search(start, pivot-1)
    '''
    pivot = findPivot(shiftArr)  # pivot is smallest integer

    if pivot == 0 or num < shiftArr[0]:
        return binarySearch(shiftArr, pivot, len(shiftArr)-1, num)

    return binarySearch(shiftArr, 0, pivot - 1, num)


def findPivot(array):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end)//2
        # Found pivot
        if mid == 0 or array[mid] < array[mid-1]:
            return mid
        if array[mid] > array[start]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def binarySearch(array, start, end, num):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == num:
            return mid
        if array[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    # num not in array
    return -1
