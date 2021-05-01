import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    ans = []

    def solve(level, idx):
        if level == m:
            print(*ans)
            return
        
        for i in range(idx, n):
            ans.append(i+1)
            solve(level+1, i+1)
            ans.pop()

    solve(0,0)

if __name__ == "__main__":
    sys.exit(main())