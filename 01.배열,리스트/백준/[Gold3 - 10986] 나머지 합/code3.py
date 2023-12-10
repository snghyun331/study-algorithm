# 다른 사람 풀이 2차
# 시간 568ms, 메모리 142240

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split())) 

# code2와 차이점: 누적 합을 바로바로 업뎃한 후 C리스트에 카운트 추가
pSum = 0 
C = [0] * m
for i in range(n):
    pSum = (pSum + A[i]) % m  # 누적 합을 업데이트할 때 (pSum + A[i]) % m을 바로 pSum에 대입하여 처리.
    C[pSum] += 1

answer = 0
for i in range(m):
    if i == 0:  
        answer += C[i] * (C[i] + 1) // 2   
    else: answer += C[i] * (C[i] - 1) // 2
print(answer)