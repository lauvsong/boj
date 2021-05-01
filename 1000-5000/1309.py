import sys
input = sys.stdin.readline

MOD = 9901
N = int(input())
dp = [[0]*(3) for _ in range(N)]

no, left, right = [0]*N, [0]*N, [0]*N
no[0] = 1; left[0] = 1; right[0] = 1;

for i in range(1,N):
    no[i] = (no[i-1] + left[i-1] + right[i-1]) % MOD
    left[i] = (no[i-1] + right[i-1]) % MOD
    right[i] = (no[i-1] + left[i-1]) % MOD

print((no[-1]+left[-1]+right[-1]) % MOD)


"""
동물원

no = no+left+right
left = no+right
right = no+left
"""