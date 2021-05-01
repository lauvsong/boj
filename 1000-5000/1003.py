# 피보나치 수열
import sys

fib = [(0,1),(1,0)]

while len(fib) < 41:
    fib.append(tuple(map(sum, zip(fib[-1], fib[-2]))))

n = int(sys.stdin.readline())

for _ in range(n):
    i = int(sys.stdin.readline())
    print(fib[i][0], fib[i][1])