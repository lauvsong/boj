# C++로는 가능, 파이썬으로 솔브 불가
import sys
input = sys.stdin.readline

n,ans = int(input()),0
grid  = [[False]*30 for _ in range(30)]

def check(x,y):
    for i in range(x+1):
        #print(x,y,i)
        if grid[i][y] or grid[x-i][y-i] or grid[x-i][y+i]: return False
    return True

def solve(x):
    global ans
    if x == n:
        ans += 1
        return

    for y in range(n):
        if check(x,y):
            grid[x][y] = True
            solve(x+1)
            grid[x][y] = False

solve(0)
print(ans)