# 시간: 608ms

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort() 

start = 1
end = house[-1] - house[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = house[0]
    cnt = 1
    
    for i in range(1, N):
        if house[i] >= value + mid:
            value = house[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)