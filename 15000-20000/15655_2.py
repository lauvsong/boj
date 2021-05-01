import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
cache = [False]*n
ans = []

def solve(depth, idx):
    if depth == m:
        print(*ans)
        return

    for i in range(idx, n):
        if cache[i]: continue
        cache[i] = True
        ans.append(nums[i])
        solve(depth+1,i+1)
        cache[i] = False
        ans.pop()
    
solve(0,0)