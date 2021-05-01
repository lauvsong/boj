# 차이를 최대로
import sys
input = sys.stdin.readline

def solve(depth):
    global maximum
    if depth == n:
        res = 0
        for i in range(n-1):
            res += abs(ans[i] - ans[i+1])
        maximum = max(res, maximum)
        return

    for i in range(n):
        if cache[i]: continue
        cache[i] = True
        ans.append(a[i])
        solve(depth+1)
        ans.pop()
        cache[i] = False

n = int(input())
a = list(map(int, input().split()))
cache = [False]*n
maximum = -1e9
ans = []

solve(0)
print(maximum)