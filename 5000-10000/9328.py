# 열쇠
## 골드 1
## 극한의 구현 문제
from collections import deque, Counter, defaultdict
import sys
input = sys.stdin.readline

def main():
    def bfs():
        q = deque()
        q.append((0,0))
        cache = [[False]*w for _ in range(h)]
        cache[0][0] = True
        move = [(0,-1),(0,1),(1,0),(-1,0)]
        doors = defaultdict(list)
        ans = 0

        while q:
            x,y = q.popleft()
                
            for dx,dy in move:
                nx, ny = x+dx, y+dy

                if 0<=nx<h and 0<=ny<w:
                    if cache[nx][ny]: continue
                    cache[nx][ny] = True
                    if (loc := grid[nx][ny]) == '*': continue

                    # 빈 공간
                    if loc == '.':
                        q.append((nx, ny))
                    # 문서
                    elif loc == '$':
                        q.append((nx,ny))
                        grid[nx][ny] = '.'
                        ans += 1
                    # 문
                    elif loc.isupper():
                        if keys.get(loc.lower()):
                            q.append((nx,ny))
                            grid[nx][ny] = '.'
                        else:
                            doors[loc].append((nx,ny))

                    # 열쇠
                    elif loc.islower():
                        q.append((nx,ny))
                        keys[loc] = True
                        grid[nx][ny] = '.'
                        q.extend(doors[loc.upper()])

        return ans


    t = int(input())
    for _ in range(t):
        h,w = map(int, input().split())
        grid = [['.']*(w+2)]
        grid += [list('.'+input().rstrip()+'.') for _ in range(h)]
        grid += [['.']*(w+2)]

        h,w = h+2, w+2

        key = input().rstrip()
        keys = Counter(key)

        print(bfs())

if __name__ == "__main__":
    sys.exit(main())