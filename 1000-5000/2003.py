# 수들의 합 2
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = tuple(map(int, input().split()))

start, end = 0,0
res = 0
cnt = 0

while True:
    if res >= m:
        if res == m:
            cnt += 1
        res -= a[start]
        start += 1
    elif end == n:
        break
    else:
        res += a[end]
        end += 1

print(cnt)