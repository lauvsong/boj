from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = map(str,sorted(map(int, input().split())))

print("\n".join(map(" ".join, combinations(nums,m))))