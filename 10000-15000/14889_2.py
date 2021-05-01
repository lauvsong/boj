from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
grid = tuple(tuple(map(int, input().split())) for _ in range(n))
start, link = [], []
ans = sys.maxsize

for cb in combinations(range(n),n//2):
    start = cb
    link = tuple(set(range(n)) - set(cb))
    spower, lpower = 0,0

    for x,y in combinations(start,2):
        spower += grid[x][y] + grid[y][x]

    for x,y in combinations(link,2):
        lpower += grid[x][y] + grid[y][x]

    ans = min(ans, abs(spower-lpower))

print(ans)