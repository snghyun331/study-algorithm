# 시간 초과.... (슬라이싱 때문인 듯)

import sys

input = sys.stdin.readline

def merge_sort(data, left, right):
    if left < right:
        mid = (left + right ) // 2
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)
        
def merge(A, left, mid, right):
    global result
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] > A[j]:
            sortedList[k] = A[j]
            result = result + j - k
            j += 1
        else:
            sortedList[k] = A[i]
            i += 1
        k += 1
    
    if i > mid:
        sortedList[k:] = A[j:]
    else:
        sortedList[k:] = A[i:]

    A[left:right+1] = sortedList[left:right+1]

N = int(input())
A = list(map(int, input().split()))
result = 0
sortedList = [0] * N

merge_sort(A, 0, N-1)
print(result)