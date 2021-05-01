import sys
input = sys.stdin.readline

def main():
    def bfs():
        q = [(r,c)]
        cache = [[False]*n for _ in range(n)]
        cache[r][c] = True
        ans = 0

        while q:
            tmp = []

            for x,y in q:
                if x == tr and y == tc: return ans
                
                for loc in ((x-2,y-1),(x-2,y+1),(x,y-2), (x,y+2),(x+2,y-1),(x+2,y+1)):
                    nx, ny = loc
                    if 0<=nx<n and 0<=ny<n:
                        if cache[nx][ny]: continue
                        tmp.append((nx,ny))
                        cache[nx][ny] = True

            q = tmp
            ans += 1

        return -1

    n = int(input())
    r,c,tr,tc = map(int, input().split())

    print(bfs())

if __name__ == "__main__":
    sys.exit(main())