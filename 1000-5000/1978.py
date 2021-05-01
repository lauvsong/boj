import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
nums = set(map(int, input().split())) - set(range(0,2))

for i in range(2, int(1000**0.5)+1):
    nums -= set(range(i*2, 1000+1, i))

print(len(nums))