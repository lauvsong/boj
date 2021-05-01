from itertools import product
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))

for i in product(nums, repeat=m):
    print(*i)