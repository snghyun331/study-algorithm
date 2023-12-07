# 입력이 끝날 때까지 계속
import sys

while(True):    
    try:
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break