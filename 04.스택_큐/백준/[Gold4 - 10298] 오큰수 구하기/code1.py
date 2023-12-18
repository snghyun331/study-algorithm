# 나의 풀이
# 시간 1148ms 메모리 155544kb

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
resultList = [0] * N

for i in range(N):
    while stack and  A[stack[-1]] < A[i]:
        resultList[stack[-1]] = A[i]
        stack.pop()
        
    stack.append(i)   
   
while stack:
    resultList[stack[-1]] = -1
    stack.pop()
    
print(*resultList)


        
        