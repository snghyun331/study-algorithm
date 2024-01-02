# 병합 정렬1 (교재)
# 시간 48ms, 메모리 31120

import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

sortedList = [0] * len(data)

def merge(A, left, mid, right):
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sortedList[k] = A[i]
            i += 1
        else:
            sortedList[k] = A[j]
            j += 1
        k += 1
        
    if i > mid:
        sortedList[k:] = A[j:]
    else:
        sortedList[k:] = A[i:]
    
    A[left:right+1] = sortedList[left:right+1]
    

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right ) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

    
merge_sort(data, 0, len(data) - 1)

for d in data:
    print(d)
