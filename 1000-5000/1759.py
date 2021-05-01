from itertools import combinations
import sys
input = sys.stdin.readline

l,c = map(int, input().split())
crypto = sorted(input().split())
a = {'aeiou'}
for cb in combinations(crypto, l):
    tmp = set(cb) - a
    if len(tmp) < 2 or l-len(tmp) < 1: continue
    print("".join(cb))