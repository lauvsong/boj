import sys
input = lambda: sys.stdin.readline().strip().split()

A,B,C = map(int, input())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')