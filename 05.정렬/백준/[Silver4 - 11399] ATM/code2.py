# 삽입 정렬로 풀어봄
# 시간 88ms

import sys

input = sys.stdin.readline

N = int(input())   
P = list(map(int, input().split()))   

for i in range(1, N):
    key = P[i]
    j = i - 1
    while j >= 0 and P[j] > key:
        P[j+1] = P[j]
        j -= 1
    P[j + 1] = key
    
Sum = 0
S = []
for i in range(N):
    Sum = Sum + P[i]   
    S.append(Sum)
                    # 최종 S: [1,3,6,9,13]
print(sum(S))

        