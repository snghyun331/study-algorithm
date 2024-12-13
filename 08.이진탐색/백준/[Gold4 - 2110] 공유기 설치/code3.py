# 내가 정리해서 푼 코드
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()
start = 1
end = house[-1] - house[0]
result = 0

if (C == 2):
    print(house[-1] - house[0])
else:
    while (start <= end):
        C_cnt = 1
        ts = house[0]
        mid = (start + end) // 2
        # 공유기 개수만 일단 늘려보기
        for i in range(N):
            if house[i] - ts >= mid:
                C_cnt += 1
                ts = house[i]

        # 집들 순회가 모두 끝난 후
        if C_cnt >= C: # 목표한 것보다 더 설치 가능하면 -> 거리를 늘려보기
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)

                
