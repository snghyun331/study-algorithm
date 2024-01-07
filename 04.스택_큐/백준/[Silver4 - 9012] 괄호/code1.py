# 시간 44ms, 메모리 31120KB

import sys

input = sys.stdin.readline

T = int(input())

def check(test):
    stack = []
    for t in test:
        if t == "(":
            stack.append(t)
        if t == ")":
            if len(stack) == 0:  # 조건1 위배
                return "NO"    
            else:
                stack.pop()
        
    if len(stack) != 0:  # 조건2 위배
        return "NO"
    else:
        return "YES"

for i in range(T):
    test = list(input().strip())
    print(check(test))