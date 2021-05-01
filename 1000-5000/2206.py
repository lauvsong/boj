import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    grid = tuple(input().rstrip() for _ in range(n))
    dx, dy = [1,-1,0,0], [0,0,1,-1]

    def bfs():
        cache = [[2]*m for _ in range(n)]
        q = [(0,0,0)]
        cache[0][0] = 0
        dist = 1

        while q:
            tmp = []
            for x,y,chance in q:

                if x == n-1 and y == m-1: return dist
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]

                    if 0 <= nx <n and 0 <= ny <m:
                        if cache[nx][ny] > chance:
                            if grid[nx][ny] == '1' and chance != 1:
                                cache[nx][ny] = 1
                                tmp.append((nx,ny,1))
                            elif grid[nx][ny] == '0':
                                cache[nx][ny] = chance
                                tmp.append((nx,ny,chance))
            
            q = tmp
            dist += 1
        return -1

    print(bfs())

if __name__ == "__main__":
    sys.exit(main())