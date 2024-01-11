# 시간 64ms, 메모리 34052kb

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
Rs = [int(input()) for _ in range(N)]  # 주차 공간 번호 순의 단위 요금
Wk = [int(input()) for _ in range(M)]  # 차량 번호 순의 무게
InOut = [int(input()) for _ in range(M*2)]  # 차량들이 들어가고 나가는 순서 저장
dq = deque()  # 대기장소 큐
parking_lot = [0] * N  # 주차장 (처음에는 모두 비어있음)
price = 0  # 주차 요금
    
for car in InOut:
    if car > 0:  # 양수이면 들어오는 차량
        dq.append(car)
        if 0 not in parking_lot:  # 주차 공간 full
            pass
        else:
            x = parking_lot.index(0)  
            parking_lot[x] = dq.popleft()   # 맨 왼쪽부터 탐색에 처음 0인 인덱스 구간에 popleft한 차량 번호 집어넣기
            price = price + (Rs[x] * Wk[car-1])  # 주차된 공간에 해당하는 단위 요금 X 차량 무게
    else:  # 음수이면 나가는 차량
        car = abs(car) 
        parking_lot[parking_lot.index(car)] = 0  # 차량이 나간 주차 공간은 다시 0으로
        if(dq):  # 대기 큐에 대기하는 차량이 있으면 그 즉시 맨 앞쪽 차량만 popleft하여 0인 공간에 집어넣기
            x = parking_lot.index(0)
            car = dq.popleft()
            parking_lot[x] = car
            price = price + (Rs[x] * Wk[car-1])
        
        
print(price)

