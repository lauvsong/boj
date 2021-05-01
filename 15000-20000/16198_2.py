import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
w = tuple(map(int, input().split()))

def dfs(arr):
    if len(arr) == 3:
        return arr[0]*arr[2]

    ans = 0
    for i in range(1, len(arr)-1):
        res = arr[i-1]*arr[i+1] + dfs(arr[:i] + arr[i+1:])
        ans = max(res, ans)

    return ans

print("%d" % dfs(w))