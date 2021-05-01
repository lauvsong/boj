import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = []

def solve(depth):
    if depth == m:
        print(*ans)
        return

    for i,num in enumerate(nums):
        ans.append(num)
        solve(depth+1)
        ans.pop()

solve(0)