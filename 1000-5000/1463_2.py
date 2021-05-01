import sys
input = sys.stdin.readline

def dp(n):
    global ans
    if n == 1:
        return ans

n = int(input())
ans = 0