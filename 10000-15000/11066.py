import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    page = tuple(map(int, input().split()))

    dp = [[0]*k for _ in range(k)]
    for i in range(k-1):
        dp[i][i+1] = page[i] + page[i+1]
        for j in range(i+2,k):
            dp[i][j] = dp[i][j-1] + page[j]

    for d in range(2,k):
        for i in range(k-d):
            j = i+d
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i,j)]
            dp[i][j] += min(minimum)

    print(dp[0][k-1])

"""
dp[i][j] : i부터 j까지 파일을 하나로 합치는데 드는 최소 비용

dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]) + sum(files[i]~files[j]))
총 3중 for문 필요
i : 시작점 (1, )
j : 끝점 
k : 개수 
"""