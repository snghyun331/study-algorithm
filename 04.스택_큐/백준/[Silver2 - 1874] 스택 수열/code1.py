# 시간 188ms, 메모리 36560KB

import sys

input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
ans = []  # +, - 결과를 우선 리스트에 저장하는 이유: 만약 불가능한 경우 "NO"만 출력해야해서

stack = []
index = 0   # 수열의 인덱스
for i in range(1,n+1):   # 1부터 n까지 push 반복
    stack.append(i)
    ans.append('+')
    while stack and sequence[index] == stack[-1]:  # 수열의 값 = 현재 스택의 마지막 값
        stack.pop()
        ans.append('-')
        index += 1    # pop연산이 수행되면, 비교해야하는 index는 1씩 증가
        
if len(stack) != 0:   # 1~n의 push가 모두 끝났는데도 스택이 비어있지 않다면,
    print("NO")
else:                 # 스택이 비어있으면,
    for ch in ans:    # +, - 한꺼번에 출력
        print(ch)    
