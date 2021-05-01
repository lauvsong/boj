import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    cache = [False]*n
    ans = []

    def solve(depth):
        if depth == m:
            print(*ans)
            return
        
        for i,num in enumerate(nums):
            if cache[i]: continue
            cache[i] = True
            ans.append(num)
            solve(depth+1)
            cache[i] = False
            ans.pop()

    solve(0)

if __name__ == "__main__":
    sys.exit(main())