import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = []

def solve(depth, idx):
    if depth == m:
        print(*ans)
        return

    prev = -1
    for i in range(idx,n):
        if nums[i] == prev: continue
        ans.append(nums[i])
        solve(depth+1, i+1)
        ans.pop()
        prev = nums[i]

solve(0,0)