import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = set()
tmp = []
cache = [False]*n

def solve(depth):
    if depth == m:
        ans.add(tuple(tmp))
        return

    for i,num in enumerate(nums):
        if cache[i]: continue
        cache[i] = True
        tmp.append(num)
        solve(depth+1)
        cache[i] = False
        tmp.pop()

solve(0)
for a in sorted(ans):
    print(*a)