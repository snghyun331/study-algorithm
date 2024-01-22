# 시간 92ms, 메모리 34036KB

import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
truck_weights = list(map(int, input().split()))

truck_weights = deque(truck_weights)
bridge = [0] * w
bridge = deque(bridge)
ans = 0
current_weight = 0

while len(truck_weights) > 0:
    ans += 1
    current_weight = current_weight - bridge.popleft()
    if current_weight + truck_weights[0] <= L:
        current_weight += truck_weights[0]
        bridge.append(truck_weights.popleft())
    else:
        bridge.append(0)
        
ans += w
print(ans)       

