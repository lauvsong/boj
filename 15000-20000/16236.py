import sys
input = sys.stdin.readline

def main():
    def bfs():
        cache = {(sx,sy)}
        q = [(sx,sy)]

        shark = 2
        eat = 0
        ans, tick = 0, 0
        term = False

        while q:
            q.sort()
            tmp = []

            for x,y in q:
                if (prey := grid[x][y]) and prey < shark:
                    grid[x][y] = 0
                    eat += 1
                    ans = tick

                    if eat == shark:
                        shark += 1
                        eat = 0
                    
                    q = [(x,y)]
                    tmp = []
                    cache = {(x,y)}
                    term = True
                
                for dx,dy in ((-1,0),(0,-1),(0,1),(1,0)):
                    nx,ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if (nx,ny) in cache: continue
                        if grid[nx][ny] > shark: continue
                        tmp.append((nx,ny))
                        cache.add((nx,ny))

                if term:
                    term = False
                    break

            q = tmp
            tick += 1
        return ans


    grid = []
    n = int(input())

    for i in range(n):
        tmp = list(map(int, input().split()))
        grid.append(tmp)

        for j in range(n):
            if tmp[j] == 9:
                sx, sy = i, j
                grid[sx][sy] = 0
                

    print(bfs())

if __name__ == "__main__":
    sys.exit(main())