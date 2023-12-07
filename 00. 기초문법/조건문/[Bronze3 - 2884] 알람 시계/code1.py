# 나의 풀이
# 시간 40ms, 메모리 31120kb, 길이 267B

import sys

hour, min = map(int, sys.stdin.readline().split())
early = 45

if (min-early >= 0):
    print(hour, min-early)
else:
    min = 60 - abs(min-early)
    hour -= 1
    if hour < 0:
        hour = 23
        print(hour, min)
    else:
        print(hour, min)

    

