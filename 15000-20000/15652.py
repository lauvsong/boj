import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    ans = []

    def solve(depth, idx):
        if depth == m:
            print(*ans)
            return

        for i in range(idx,n):
            ans.append(i+1)
            solve(depth+1,i)
            ans.pop()

    solve(0,0)

if __name__ == "__main__":
    sys.exit(main())