# 로또
import sys
input = sys.stdin.readline

def dfs(depth, idx):
    if depth == 6:
        print(*ans)
        return

    for i in range(idx,len(s)):
        ans.append(s[i])
        dfs(depth+1,i+1)
        ans.pop()

while True:
    s = list(map(int, input().split()))
    if (k := s[0]) == 0: break
    s = sorted(s[1:])
    ans = []
    dfs(0,0)
    print()

# 조합 재귀