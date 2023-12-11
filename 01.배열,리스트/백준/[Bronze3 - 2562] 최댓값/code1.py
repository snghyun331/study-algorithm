import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

Max = max(arr)

MaxIndex = arr.index(Max)

print(Max)
print(MaxIndex + 1)