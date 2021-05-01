from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
perm = tuple(map(int, input().split()))
gen = permutations(sorted(perm), n)
for p in gen:
    if p == perm: 
        try: print(*next(gen))
        except: print(-1)
        break