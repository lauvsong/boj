from itertools import combinations
from math import gcd
import sys
input = lambda: sys.stdin.readline()

n = int(input())
for _ in range(n):
    cnt = 0
    nums = list(map(int, input().split()))
    print(sum(gcd(x,y) for x, y in combinations(nums[1:], 2)))