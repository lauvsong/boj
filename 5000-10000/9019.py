# DSLR
import sys
input = sys.stdin.readline

def bfs(a,b):
    q = [(a,"")]
    cache = [False]*10000
    cache[a] = True

    while q:
        tmp = []

        for n,his in q:
            if n == b: return his

            # D
            res = n*2
            if res > 9999: res %= 10000
            if not cache[res]:
                cache[res] = True
                tmp.append((res, his+"D"))
            # S
            res = n-1 if n != 0 else 9999
            if not cache[res]:
                cache[res] = True
                tmp.append((res, his+"S"))
            # L
            res = (n % 1000)*10 + n // 1000
            if not cache[res]:
                cache[res] = True
                tmp.append((res, his+"L"))
            # R
            res = (n % 10)*1000 + n // 10
            if not cache[res]:
                cache[res] = True
                tmp.append((res, his+"R"))

        q = tmp

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(bfs(a,b))