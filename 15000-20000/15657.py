import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = []

def solve(depth,idx):
    if depth == m:
        print(*ans)
        return

    for i in range(idx,n):
        ans.append(nums[i])
        solve(depth+1,i)
        ans.pop()

solve(0,0)