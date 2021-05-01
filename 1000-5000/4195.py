import sys
input = sys.stdin.readline

t = int(input())

def union(a,b):
    x = find(a)
    y = find(b)

    if x == y: return
    if x < y: 
        p[y] = x
        cnt[x] += cnt[y]
    else: 
        p[x] = y
        cnt[y] += cnt[x]

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

for _ in range(t):
    f = int(input())
    p = dict()
    cnt = dict()

    for _ in range(f):
        a,b = input().split()
        if not p.get(a):
            p[a] = a
            cnt[a] = 1
        if not p.get(b):
            p[b] = b
            cnt[b] = 1

        union(a,b)

        print(cnt[find(a)])