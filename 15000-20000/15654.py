from itertools import permutations
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    print("\n".join(map(" ".join, permutations(map(str, nums), m))))

if __name__ == "__main__":
    sys.exit(main())