import sys
input = sys.stdin.readline

t = int(input())
n = tuple(int(input()) for _ in range(t))
MOD = 1000000009

odd = [0,1,1,2]
even = [0,0,1,2]

for i in range(4,max(n)+1):
    odd.append((even[i-1]+even[i-2]+even[i-3]) % MOD)
    even.append((odd[i-1]+odd[i-2]+odd[i-3]) % MOD)

for v in n:
    print(odd[v], even[v])

"""
홀/짝 여부 저장해야함.
dp[i][j]
i : 홀/짝
j : 탐색중인 수
dp[EVEN][j] += dp[ODD][j-1]....[j-3]
dp[ODD][j] += dp[EVEN][-3:]
"""