# 병합 정렬2
# 시간: 44ms, 메모리: 31252	

import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    sorted_arr = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    sorted_arr += left_arr[i:]
    sorted_arr += right_arr[j:]
    return sorted_arr


sortedList = merge_sort(data)
for d in sortedList:
    print(d)