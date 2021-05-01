from itertools import permutations
import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in permutations(list(map(str, range(1, int(input())+1)))):
    print(" ".join(i)+"\n")