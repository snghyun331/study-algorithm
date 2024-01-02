# 삽입 정렬(n^2)
# 시간: 140ms, 메모리: 31120

import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

n = len(data)

for i in range(1, n):
	key = data[i]  # 선택된 데이터 (data[0]은 이미 정렬되어있으므로 data[1]부터 시작
	j = i -1  # 비교할 인덱스이자 초기에는 맨 뒤 인덱스. 따라서 data[j]는 맨 뒤 인덱스의 데이터 값
	while j >= 0 and data[j] > key:
		data[j+1] = data[j]  # 한 칸 뒤로 이동 (shift 연산)
		j = j-1 

	# 탐색이 종료되면,
	data[j+1] = key   # 선택 데이터를 제 위치에 삽입


for d in data:
    print(d)