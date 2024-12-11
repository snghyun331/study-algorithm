# 시간: 544ms

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort() # 좌표 정렬 먼저!

result = 0  # 가장 인접한 두 공유기 사이의 거리의 최댓값을 저장하는 변수
start = 1  # 공유기 사이 거리의 최소값 (최소 거리 1부터 시작)
end = house[-1] - house[0]  # 공유기 사이 거리의 최대값 (집 중 가장 먼 두 좌표의 거리)

# 공유기가 2개라면, 두 집 사이의 거리 바로 출력
if (C == 2):
    print(end)
else:
    while (start < end):
        mid = (start + end) // 2  # 현재 확인하는 거리 (공유기 간 최소 거리의 후보
        C_cnt = 1 # 실제 설치된 공유기의 개수 (C는 설치 목표 개수)
        ts = house[0]  # 마지막으로 공유기를 설치한 집의 좌표 (현재는, 첫 번째 공유기를 첫 번째 집에 설치)
        
        # 집 좌표 h[i]에서 마지막 공유기가 설치된 집 ts까지의 거리가 mid 이상이면 공유기를 설치.
        for i in range(N):
            if (house[i]- ts >= mid):
                C_cnt += 1  # 설치 가능한 집의 개수 1증가
                ts = house[i]  # 공유기를 설치한 집의 좌표 업데이트

        # 설치한 공유기의 개수(C_cnt)가 목표 개수(C) 이상이면 더 큰 거리를 시도
        if (C_cnt >= C):
            result = mid
            start = mid + 1
        # 설치한 개수가 부족하면 거리를 줄임
        else:
            end = mid

    print(result)
            

            
            
