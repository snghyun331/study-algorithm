### 입출력 함수
n1 = int(input())
print(n1+3)
# 4
# 7

n2 = input().split()
print(n2)
# 123 456
# ['123', '456']


a, b = map(int, input().split())   # 두 입력값을 int로 전환
print(a)
print(b+10)
# -1 1
# -1
# 11


### 빠른 입출력 합수

for _ in range(10000):
    n3 = int(input())
    print(n3)

# ↓ 아래 방법을 더 선호    
import sys
for _ in range(10000):
    n3 = int(sys.stdin.readline())
    print(n3)