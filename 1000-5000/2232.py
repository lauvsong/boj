import sys
input = sys.stdin.readline

def main():
    def bfs(a,b,mask):
        q = [(a,b)]
        masked[a][b] = mask
        cnt = 1

        while q:
            tmp = []
            for x,y in q:

                for i in range(4):
                    if naive[x][y] & (1 << i): continue

                    nx, ny = x+move[i][0], y+move[i][1]
                    if 0 <= nx < m and 0 <= ny < n:
                        if masked[nx][ny] != -1: continue
                        masked[nx][ny] = mask
                        tmp.append((nx, ny))
                        cnt += 1

            q = tmp
        return cnt


    n,m = map(int, input().split())
    naive = tuple(tuple(map(int, input().split())) for _ in range(m))
    masked = [[-1]*n for _ in range(m)]
    move = tuple(((0,-1), (-1,0), (0,1), (1,0)))
    area = []
    rooms = 0

    for i in range(m):
        for j in range(n):
            if masked[i][j] == -1:
                area.append(bfs(i,j,rooms))
                rooms += 1

    combined = 0
    for i in range(m):
        for j in range(n):
            if i and masked[i-1][j] != masked[i][j]:
                combined = max(combined, area[masked[i-1][j]] + area[masked[i][j]])
            if j and masked[i][j-1] != masked[i][j]:
                combined = max(combined, area[masked[i][j-1]] + area[masked[i][j]])


    print(rooms)
    print(max(area))
    print(combined)

if __name__ == "__main__":
    sys.exit(main())