import sys
input = sys.stdin.readline

n,m = map(int, input().split())
trees = tuple(map(int, input().split()))

l,r = 0, max(trees)
ans = 0

while l <= r:
    mid = (l+r) // 2
    res = 0
    for tree in trees:
        if tree > mid:
            res += (tree - mid)
    
    if res < m:
        r = mid - 1
    else:
        ans = mid
        l = mid + 1

print(ans)

"""
이진 탐색

적어도 m미터의 나무.

높이
최소: 1, 최대: max(trees)
"""