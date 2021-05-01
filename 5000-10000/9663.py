# PyPy3 로만 가능
import sys
input = sys.stdin.readline

n,ans = int(input()),0
a,b,c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(x):
    global ans
    if x == n:
        ans += 1
        return

    for y in range(n):
        if not (a[y] or b[x+y] or c[x-y+n-1]):
            a[y] = b[x+y] = c[x-y+n-1] = True
            solve(x+1)
            a[y] = b[x+y] = c[x-y+n-1] = False

solve(0)
print(ans)