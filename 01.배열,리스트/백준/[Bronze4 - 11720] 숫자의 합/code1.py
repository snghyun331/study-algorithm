# 나의 풀이
# 인덱스 번호 이용하여 풀기
# 시간 40ms, 메모리 31252kb, 길이 177B

import sys

n = int(sys.stdin.readline())
data = list(sys.stdin.readline().strip())
new_data = []

for i in range(n):
    new_data.append(int(data[i]))
    
print(sum(new_data))
