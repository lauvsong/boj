from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    for comb in combinations(range(1,n+1), m): print(*comb)

if __name__ == "__main__":
    sys.exit(main())