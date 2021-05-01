from itertools import combinations
import sys
input = sys.stdin.readline
#print = sys.stdout.write

N, S = map(int, input().split())
seq = list(map(int, input().split()))
answer = 0
for i in range(1,N+1):
    for j in combinations(seq, i):
        if sum(j) == S: answer += 1

print(answer)