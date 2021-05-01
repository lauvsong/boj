from itertools import combinations
import sys
input = sys.stdin.readline
#print = sys.stdout.write

n,m = map(int, input().split())
city = tuple(tuple(map(int, input().split())) for i in range(n))
chicken = []
house = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

for comb in combinations(chicken, m):
    dist = 0
    for x,y in house:
        dist += min(tuple(abs(x-c[0])+abs(y-c[1]) for c in comb))
        if dist >= ans: break
    ans = min(dist, ans)

print(ans)