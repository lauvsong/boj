from itertools import combinations
import sys
input = sys.stdin.readline
print = sys.stdout.write

h,w = map(int, input().split())
n = int(input())
sticker = tuple(tuple(map(int, input().split())) for _ in range(n))
ans = 0

for comb in combinations(sticker, 2):
    a,b = comb
    ax, ay, bx, by = a[0], a[1], b[0], b[1]

    # 가로 x 가로
    if ax + bx <= w and max(ay, by) <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 가로 회전
    elif ax + by <= w and max(ay, bx) <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 세가
    elif ay + bx <= w and max(ax, by) <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 세세
    elif ay + by <= w and max(ax, bx) <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 가로 x 가로
    elif max(ax, bx) <= w and ay + by <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 가로 회전
    elif max(ax, by) <= w and ay + bx <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 세가
    elif max(ay, bx) <= w and ax + by <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue
    # 세세
    elif max(ay, by) <= w and ax + bx <= h:
        ans = max(ans, (ax*ay)+(bx*by))
        continue

print("%d" % ans)