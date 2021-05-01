from math import gcd
import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    a = tuple(map(int, input().split()))

    ans = abs(a[0]-m)
    for i in a[1:]:
        tmp = gcd(ans, abs(m-i))
        ans = tmp

    print(ans)

if __name__ == "__main__":
    sys.exit(main())