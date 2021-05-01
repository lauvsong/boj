import sys
input = sys.stdin.readline

n = int(input())
nums = [False, False] + [True] * (n-1)

for i in range(2,int(n**0.5)+1):
    if nums[i]:
        for j in range(i*i, n+1, i):
            nums[j] = False

prime = [x for x in range(2,n+1) if nums[x]]

start, end = 0,0
res = 0
ans = 0

while True:
    if res >= n:
        if res == n: ans += 1
        res -= prime[start]
        start += 1

    elif end == len(prime):
        break
    else:
        res += prime[end]
        end += 1

print(ans)