import sys
from collections import deque

def binary_search(arr, target, start, end):
    while(start<= end):
        mid = (start + end) // 2
        if (target == arr[mid]):
            return mid
        elif (target <= arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return None
    


input = sys.stdin.readline

N = int(input())
part_list = deque(list(map(int, input().split())))
M = int(input())
request_list = deque(list(map(int, input().split())))

result = deque()

while(request_list):
    target = request_list.popleft()
    data = binary_search(part_list, target, 0, len(part_list) - 1)

    if (data == None):
        result.append('NO')
    else:
        result.append('YES')

for str in result:
    print(str, end=' ')