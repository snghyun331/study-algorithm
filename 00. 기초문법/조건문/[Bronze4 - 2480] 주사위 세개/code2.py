# 다른 사람 풀이
# (시간40ms, 메모리 31120KB, 길이269B)

import sys

a,b,c = map(int, sys.stdin.readline().split())
award = 0

if a==b==c:
    award = 10000 + a*1000
elif a==b:
    award = 1000 + a*100
elif b==c:
    award = 1000 + b*100
elif a==c:
    award = 1000 + a*100
else:
    award = max(a,b,c) * 100
    
print(award)