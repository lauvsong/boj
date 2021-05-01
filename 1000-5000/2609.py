import sys
input = lambda: sys.stdin.readline().split()

def gcd_lcm(x,y):
    while y:
        x,y = y, x%y
    gcd = x
    lcm = (a*b) // gcd
    return gcd, lcm

a,b = map(int, input())
print(*gcd_lcm(a,b), sep="\n")