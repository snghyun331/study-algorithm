# 시간 188ms, 메모리 36560KB

import sys

input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
ans = []

stack = []
index = 0
for i in range(1,n+1):
    stack.append(i)
    ans.append('+')
    while stack and sequence[index] == stack[-1]:
        stack.pop()
        ans.append('-')
        index += 1
if len(stack) != 0:
    print("NO")
else:
    for ch in ans:
        print(ch)    
