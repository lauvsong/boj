import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = []
cache = [False]*n

def solve(depth):
    if depth == m:
        print(*ans)
        return

    prev = -1
    for i,num in enumerate(nums):
        if cache[i]: continue
        if num == prev: continue
        cache[i] = True
        ans.append(num)
        solve(depth+1)
        cache[i] = False
        ans.pop()
        prev = num

solve(0)