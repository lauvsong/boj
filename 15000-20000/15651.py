from itertools import product
import sys
input = sys.stdin.readline

def solve():
    n,m = map(int, input().split())
    li = map(str, range(1,n+1))
    print("\n".join(list(map(" ".join, product(li, repeat=m)))))

if __name__ == "__main__":
    sys.exit(solve())