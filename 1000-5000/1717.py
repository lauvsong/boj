# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

def union(a,b):
    x = find(a)
    y = find(b)

    if x == y: return
    if x < y: p[x] = y
    else: p[y] = x

n,m = map(int, input().split())
p = [i for i in range(n+1)]

for _ in range(m):
    op,a,b = map(int, input().split())
    if op == 0:
        union(a,b)
    else:
        print("YES" if find(a) == find(b) else "NO")

"""
유니온 파인드
"""