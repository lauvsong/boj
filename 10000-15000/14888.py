# 연산자 끼워넣기
import sys
input = sys.stdin.readline

def cacs(a,op,b):
    if op == 0: return a+b
    if op == 1: return a-b
    if op == 2: return a*b
    if op == 3:
        if a < 0: return -(-a//b)
        return a//b
        
def solve(idx, res):
    global maximum, minimum
    if idx == n-1:
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return

    for j,op in enumerate(OP):
        if op == 0: continue       
        OP[j] -= 1
        solve(idx+1, cacs(res,j,a[idx+1]))
        OP[j] += 1


n = int(input())
a = list(map(int, input().split()))
OP = list(map(int, input().split()))
maximum, minimum = -1e9, 1e9

solve(0,a[0])
print(maximum, minimum, sep="\n")

# 순열 백트래킹.