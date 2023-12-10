# 다른 사람 풀이 1차
# 시간 772ms, 메모리 142240

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split())) # 원본 리스트 선언
S = [0] * n   # 누적 합 리스트 선언
C = [0] * m   # 같은 나머지의 인덱스를 카운트하는 리스트 (만약 m이 3이라면 3개의 인덱스를 가진 리스트가 되며, 나머지1이 2개 선택되면 1인덱스가 1증가한다.)

answer = 0   # 정답 변수 선언

# 1. 누적 합 배열 채우기
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]
    
# 2. C배열 업데이트 (C배열은 나머지의 카운트 값이 저장되는 리스트)
for i in range(n):
    remainder = S[i] % m   # 합배열(S)을 m으로 나눈 나머지 값
    if remainder == 0:     # 나머지가 0이면, 바로 정답 카운트
        answer += 1
    C[remainder] += 1     
    
# 3. C배얼에서, 2개의 같은 원소를 뽑는 경우의 수를 정답에 카운트
for i in range(m):
    if C[i] > 1:   # 카운트 값이 2 이상일 때, 즉 같은 나머지가 2개 이상일 때
        answer += (C[i] * (C[i]-1) // 2)
        
print(answer)
    
    


