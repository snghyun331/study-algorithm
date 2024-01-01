# .sort() 사용
# 시간 44ms

import sys

input = sys.stdin.readline

N = int(input())   # 5
P = list(map(int, input().split()))   # [3,1,4,3,2]

P.sort()  # [1,2,3,3,4]
Sum = 0
S = []
for i in range(N):
    Sum = Sum + P[i]   
    S.append(Sum)
                    # 최종 S: [1,3,6,9,13]
print(sum(S))

