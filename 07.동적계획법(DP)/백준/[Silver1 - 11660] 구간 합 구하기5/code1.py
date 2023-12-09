# 다른 사람 풀이 1차
# 시간 1112(1020)ms, 메모리 105344kb

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

A = [[0] * (N+1)]  # 원본배열, 일단 일차원 배열로 선언
# [[0,0,0,0,0]]
D = [[0] * (N+1) for _ in range(N+1)]  # 구간 합 배열, 2차원 배열로 선언
# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]


# 1. 원본 배열 만들기
for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    # input: 1 2 3 4
    # result: [0,1,2,3,4] 
    # A배열의 양 옆 사이드를 0으로 채움
    A.append(A_row)  # 한 행씩 추가


# 2. 구간 합 배열 만들기    
for i in range(1, N+1):  # 행 옮기기
    for j in range(1, N+1):  # 열 옮기기, i행 1~4열 순으로 하나씩 채워나가기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 3. 질의에 대한 답 구하기        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
    
