# 다른 사람 풀이
# 시간44ms, 메모리 31120, 길이 250B

import sys

hour, min = map(int, sys.stdin.readline().split())
add = int(sys.stdin.readline())

end_h = (hour + ((min + add) // 60)) % 24
end_m = (min + add) % 60

print(end_h, end_m)