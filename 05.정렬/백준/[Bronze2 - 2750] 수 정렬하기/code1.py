# sort함수
# 시간 44ms, 메모리 31120

import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

data.sort()

for d in data:
    print(d)