import sys
input = sys.stdin.readline

def main():
    n = int(input())
    first, *nums, target = tuple(map(int, input().split()))

    dp = [[0]*21 for _ in range(n)]
    dp[1][first] = 1

    for i,num in enumerate(nums, start=1):
        for j in range(21):
            if 0 <= j+num <= 20:
                dp[i+1][j+num] += dp[i][j]
            if 0 <= j-num <= 20:
                dp[i+1][j-num] += dp[i][j]

    print(dp[n-1][target])

if __name__ == "__main__":
    sys.exit(main())