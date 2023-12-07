# 다른 사람 풀이
# 시간40ms, 메모리 31120, 길이 445B

import sys

hour, min = map(int, sys.stdin.readline().split()) # 시작 시간, 시간 분
add = int(sys.stdin.readline()) # 필요 분

hour = hour + (add // 60)  # 몫만큼 시 더해줌
min = min + (add % 60)     # 나머지만큼 분 더해줌

if (min >= 60):  # 나머지 만큼 더한 후의 분 값이 60이상이면
    min = min - 60
    hour += 1
    
if hour >= 24:
    hour = hour - 24
    
print(hour, min)