# 나의 풀이
# 시간40ms, 메모리31120kb, 길이430B

import sys

start_h, start_m = map(int, sys.stdin.readline().split()) # 시작 시간, 시간 분
cook_m = int(sys.stdin.readline()) # 필요 분

if start_m + cook_m < 60:  # 시침을 넘기지 않을 때
    end_h = start_h   
    end_m = start_m + cook_m
else:  # 시침을 넘길 때
    for i in range(1,1000):  # i: 시침 넘기는 횟수, 범위는 무한대로 (어차피 break걸기 때문에)
        if (60*i <= start_m + cook_m < 60*(i+1)):
            end_h = start_h + i   # 시침 넘기는 횟수만큼 시작 시간을 더해준다
            end_m = (start_m + cook_m - 60*i)
            break

if end_h >= 24:
    end_h = end_h - 24
    
print(end_h, end_m)




