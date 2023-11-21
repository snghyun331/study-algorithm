# DFS, BFS, 백트래킹

**인접행렬 vs 인접리스트**  
→ Notion

## DFS(깊이 우선 탐색)

: 완전탐색, 모든 경우의 수를 탐색, 스택이나 재귀를 사용해서 구현

- 가볼 수 있는 노드로 진행하고, 또 갈 수 있는 노드가 존재하면 계속 진행하다가, 더 갈 수 없으면 올라오는 방식

```python
adj = [[0]*13 for _ in range(13)]  # adjacent 인접 행렬
adj[0][1] = adj[0][7] = 1    # 1,7이 같은 레벨
adj[1][2] = adj[1][5] = 1    # 2,5가 같은 레벨
# ....
for row in adj:
    print(row)   # 인접행렬 출력

# [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```python
adj = [[0]*13 for _ in range(13)]  # adjacent 인접 행렬
adj[0][1] = adj[0][7] = 1    # 1,7이 같은 레벨
adj[1][2] = adj[1][5] = 1    # 2,5가 같은 레벨
# ....
for row in adj:
    print(row)   # 인접행렬 출력
```

```python
adj = [[0]*13 for _ in range(13)]  # adjacent 인접 행렬
adj[0][1] = adj[0][7] = 1    # 1,7이 같은 레벨
adj[1][2] = adj[1][5] = 1    # 2,5가 같은 레벨

# 재귀
def dfs(now):   # now: 현재 방문하는 노드 번호
    for next in range(13):    # 다음 방문하려는 노드
        if adj[now][next]:    # 현재에서 다음에 가려는 간선이 있으면,
            dfs(next)         # next번 노드로 탐색 진행

dfs(0)
```

## BFS(너비우선탐색)

: 완전탐색, 큐를 사용해서 구현

- DFS와의 차이점: 탐색순서가 다름

```python
from collections import deque

adj = [[0]*13 for _ in range(13)]  # adjacent 인접 행렬
adj[0][1] = adj[0][2] = 1    # 1,7이 같은 레벨
adj[1][3] = adj[1][4] = 1    # 2,5가 같은 레벨

def bfs():
    dq = deque()
    dq.append(0)   # 루트 노드 setting
    while dq:   # 덱을 반복: 덱에서 값을 하나빼고(pop) 그 노드에서 갈 수 있는 다음 노드들을 삽입(push)
        now = dq.popleft()
        for next in range(13):
            if adj[now][next]:
                dq.append(next)

bfs()
```

**dfs bfs 최단거리 문제**  
→ 왼쪽에서 시작할때 vs 오른쪽에서 시작할 때  
(bfs가 시간면에서 더 유리 - 이유: 처음 목표 노드를 만났을 때의 거리가 최단거리일 확률이 매우 높기 때문에 답을 찾으면 바로 종료함)

### (예제) 길찾기

- 방문체크 필요
- 각 칸이 노드

```python
dy = (0,1,0,-1)
dx = (1,0,-1,0)
check = [[False]*100 for _ in range(100)]
N = int(input())

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()    # 덱에서 빠진 것이 좌표를 나타냄
        check[y][x] = True   # 방문체크
        for k in range(4):   # 다음 방문을 하려는 곳은 총 후보 4개의 간선(상하좌우)
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny,nx) and not check[ny][nx]:   # 유효한 칸이면서 방문한 적없는 곳이라면,
                q.append((ny,nx))   # 한번 가보겠다.

bfs(0,0)
```
