from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    li = sorted(set(combinations(nums,m)))

    for i in li:
        print(*i)

if __name__ == "__main__":
    sys.exit(main())