# 병합 정렬3 (버블 솔트 강의 로직으로 구현)
# 시간: 44ms, 메모리: 31252KB

import sys

input = sys.stdin.readline

def merge_sort(left, right):
    if left == right:   # 크기가 1인 배열일 경우
        return
    
    mid = ( left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid+1, right)
    
    for x in range(left, right+1):   # 바로 A를 바꾸는 것보다 tmp 리스트를 만든 뒤, tmp에 A를 복사해서 tmp의 요소로 비교할 것
        tmp[x] = A[x]
        
    k = left   # 임시 리스트 인덱스
    i = left   # 왼쪽 리스트의 포인터
    j = mid + 1  # 오른쪽 리스트의 포인터
    while i <= mid and j <= right:
        if tmp[i] > tmp[j]:
            A[k] = tmp[j]
            j += 1
        else:
            A[k] = tmp[i]
            i += 1
        k += 1
    
    # 왼쪽 리스트만 아직 처리 안된 경우
    while i <= mid:
        A[k] = tmp[i]
        k += 1
        i += 1
    
    # 오른쪽 리스트만 아직 처리 안된 경우
    while j <= right:
        A[k] = tmp[j]
        k += 1
        j += 1

N = int(input())
A = [int(input()) for _ in range(N)]
tmp = [0] * N

merge_sort(0, N-1)

for a in A:
    print(a)







