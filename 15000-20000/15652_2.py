from itertools import combinations_with_replacement as cbr
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    li = map(str, range(1,n+1))
    print("\n".join(map(" ".join, cbr(li,m))))

if __name__ == "__main__":
    sys.exit(main())