# 시간 40ms, 메모리 31120

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [int(i) for i in range(1,n+1)]

for _ in range(m):
    f_index, s_index = map(int, input().split())  
    new_arr = arr[f_index-1:s_index] 
    new_arr.reverse()                
    arr[f_index-1:s_index] = new_arr

print(*arr)  # 리스트 요소를 한줄에 한번에 출력
    
    