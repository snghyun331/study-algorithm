# 다른 사람 풀이 2차
# 시간 1068(1104)ms, 메모리 105940kb

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 원본 배열 만들기
A = [list(map(int, input().split())) for _ in range(n)]  # 첫번째 행을 0으로 채우지 않음
# 1 2 3 4
# 2 3 4 5 
# 3 4 5 6
# 4 5 6 7


# 2. 구간(누적) 합 배열 구하기
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = A[i - 1][j - 1] + D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] # A의 첫번째 행을 0으로 채우지 않았기 때문에 A[i-1][j-1]

# 3. 질의에 대한 답 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)