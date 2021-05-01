from itertools import combinations_with_replacement as cbr
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))

for i in cbr(nums,m):
    print(*i)