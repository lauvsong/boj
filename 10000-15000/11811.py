from itertools import islice
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = [0]*n

    for x in range(n):
        grid = map(int, input().split())
        for i,y in enumerate(islice(grid, 0, x)):
            ans[x] |= y
            ans[i] |= y

    print(*ans)

if __name__ == '__main__':
    sys.exit(main())