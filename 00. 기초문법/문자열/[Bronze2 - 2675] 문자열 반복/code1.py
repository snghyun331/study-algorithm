# 시간 40ms, 31120

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result = ''
    R, S = input().split()
    for s in S:
        result += s*int(R)
    print(result)
        

