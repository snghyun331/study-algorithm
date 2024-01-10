# 시간 188ms, 메모리 50932KB

import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

N = int(input())
for i in range(1,N+1):
    dq.append(i)
    
while(dq):    # 큐가 비어있지 않을 때까지 반복
    for _ in range(len(dq)//2):  # 둘 씩 짝지으면 반복되는 횟수는 큐 길이의 절반으로 줄어드니까
        dq.popleft()    # 맨처음은 그냥 pop
        x = dq.popleft()   # 그 다음은 pop하면서 맨 뒤에 append
        dq.append(x)
    if len(dq) == 1:    # 큐에 숫자 하나 남았을 때 break
        break
    
print(dq[0])
        
