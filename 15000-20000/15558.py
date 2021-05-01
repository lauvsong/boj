import sys
input = sys.stdin.readline

def main():
    n,k = map(int, input().split())
    q = [(0,0)]
    dirs = [input(), input()]
    cache = [[False]*n for _ in range(2)]
    rm = 0

    while q:
        tmp = []

        for i,d in q:
            if i+1 >=n or i+k >= n:
                print(1)
                sys.exit()

            if dirs[d][i+1] == '1' and not cache[d][i+1]:
                cache[d][i+1] = True
                tmp.append((i+1,d))
            if i-1 > rm and dirs[d][i-1] == '1' and not cache[d][i-1]:
                cache[d][i-1] = True
                tmp.append((i-1,d))
            if dirs[1-d][i+k] == '1' and not cache[1-d][i+k]:
                cache[1-d][i+k] = True
                tmp.append((i+k,1-d))

        rm += 1
        q = tmp

    print(0)

if __name__ == "__main__":
    sys.exit(main())