import sys
input = sys.stdin.readline

def union(a,b):
    x = find(a)
    y = find(b)
    if x == y: return
    
    if x < y: p[x] = y
    else: p[y] = x

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

n = int(input())
m = int(input())
p = [i for i in range(n+1)]

for i in range(1,n+1):
    city = tuple(map(int, input().split()))
    for j in range(1,n+1):
        if city[j-1] == 1:
            union(i,j)

plan = tuple(map(int, input().split()))
res = set([find(i) for i in plan])
print("YES" if len(res) == 1 else "NO")