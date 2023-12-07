# count함수 이용하여 중복숫자 개수 찾아내기 
# (시간40ms, 메모리 31120KB, 길이330B)

import sys

data = list(map(int, sys.stdin.readline().split()))
award = 0

for i in range(3):  # 리스트 안의 요소를 모두 돌면서,
    if (data.count(data[i]) == 3):  # 중복 요소 개수가 3개일 경우
        award = 10000 + data[i] * 1000
        break   # 시간 절약을 위해 바로 break
    elif (data.count(data[i]) == 2):   # 중복 요소 개수가 2개일 경우
        award = 1000 + data[i] * 100
        break

if award == 0:   # 만약 중복 요소 개수가 3이나 2가 아니라서 award가 여전히 0인경우
    award = max(data)*100

    
print(award)