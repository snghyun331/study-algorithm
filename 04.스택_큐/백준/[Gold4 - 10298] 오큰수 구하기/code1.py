# 나의 풀이
# 시간 1148ms 메모리 155544kb

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
resultList = [0] * N   # result 수열 정의

for i in range(N):
    while stack and  A[stack[-1]] < A[i]:   # 오큰수 조건(스택이 비어있지 않을 때 & A[현재 Top 값] < A[append할 값] 일 때)
        resultList[stack[-1]] = A[i]  # result 수열에 저장
        stack.pop()
        
    stack.append(i)  # 오큰수일 때와 아닐 때 상관없이 무조건 append   
   
while stack:   # 스택이 비어있지는 않은데 다음 인덱스가 존재하지 않아 종료해야할 때
    resultList[stack[-1]] = -1
    stack.pop()
    
print(*resultList)


        
        