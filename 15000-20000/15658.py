# 연산자 끼워넣기 2
import sys
input = sys.stdin.readline

def cac(a,op,b):
    if op == 0:
        return a+b
    if op == 1:
        return a-b
    if op == 2:
        return a*b
    if op == 3:
        if a < 0 and b > 0:
            return -(-a // b)
        return a // b

def dfs(idx, res):
    global maximum, minimum
    if idx == n-1:
        maximum = max(maximum, res)
        minimum = min(minimum, res)
        return

    for i in range(4):
        if op[i] == 0: continue
        op[i] -= 1
        dfs(idx+1, cac(res,i,a[idx+1]))
        op[i] += 1


n = int(input())
a = tuple(map(int, input().split()))
op = list(map(int, input().split()))
maximum, minimum = -1e9,1e9

dfs(0,a[0])
print(maximum)
print(minimum)