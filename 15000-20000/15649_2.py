import sys
input = sys.stdin.readline

n,m = map(int, input().split())
cache = [False]*n
ans = []

def solve(level):
    if level == m:
        print(*ans)
        return

    for i in range(n):
        if cache[i]: continue
        cache[i] = True
        ans.append(i+1)
        solve(level+1)
        cache[i] = False
        ans.pop()

solve(0)