from math import gcd
import sys
input = sys.stdin.readline
#print = sys.stdout.write

n,m = map(int, input().split(':'))
i = gcd(n,m)

print("{}:{}".format(n//i, m//i))