from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
grid = tuple(tuple(map(int, input().split())) for _ in range(n))
start, link = [], []
ans = sys.maxsize

def solve(depth, idx):
    global ans
    if depth == n//2:
        link = [i for i in range(n) if i not in start]
        spower, lpower = 0,0

        for x,y in combinations(start,2):
            spower += grid[x][y] + grid[y][x]
        
        for x,y in combinations(link,2):
            lpower += grid[x][y] + grid[y][x]
        
        ans = min(ans, abs(spower-lpower))
        return

    for i in range(idx,n):
        start.append(i)
        solve(depth+1, i+1)
        start.pop()

solve(0,0)
print(ans)