# 나의 풀이
# 시간 620ms, 메모리 142240

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split())) # 원본 리스트 선언

pSum = 0   # pSum: 누적합을 변수로 선언
C = [0] * m
for i in range(n):
    pSum = pSum + A[i]
    remainder = pSum % m
    C[remainder] += 1

answer = 0
for i in range(m):
    if i == 0:  # 나머지가 0일 경우
        answer += C[i] * (C[i] + 1) // 2   # nC2 + n →  n X (n+1) // 2 (n는 0의 개수)
    else: answer += C[i] * (C[i] - 1) // 2
print(answer)