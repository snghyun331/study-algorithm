# 나의 풀이
# 리스트 요소 바로 꺼내서 풀기 (사실상 n은 필요없음)
# 시간 40ms, 메모리 31120kb, 길이 141B

import sys

n = int(sys.stdin.readline())
data = list(sys.stdin.readline().strip())
sum = 0

for d in data:
    sum += int(d)
    
print(sum)
