# 시간 44ms, 메모리 31120

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [int(i) for i in range(1,n+1)]

for _ in range(m):
    f_index, s_index = map(int, input().split())  # 인풋으로 인덱스 값 받음. 단, 해당 인덱스는 1을 기준으로 시작하므로, 이후 0을 기준으로 시작하는 코드를 작성해야함
    new_arr = arr[f_index-1:s_index]  # 특정 구간을 뽑아내서 
    new_arr.reverse()                 # 역순으로 바꿈
    arr[f_index-1:s_index] = new_arr

for i in arr:
    print(i, end=' ')
    
    