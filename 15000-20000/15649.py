from itertools import permutations
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    for perm in permutations(range(1,n+1),m):
        print(*perm)

if __name__ == "__main__":
    sys.exit(main())