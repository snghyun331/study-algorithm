# 마지막 0 0 이 들어오면 종료

import sys

while(True):
    a,b = map(int, sys.stdin.readline().split())
    if (a==0) and (b==0):
        break
    else:
        print(a+b)
    