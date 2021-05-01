# 퍼즐
## 맵 상태를 계속 기억하고 있어야 하는 유형.
## 해싱 솔루션 적용해야함

import sys
input = sys.stdin.readline

def main():
    goal = "123456780"
    cache = dict()
    grid = ""

    def bfs():
        ans = 0
        move = [(0,-1),(0,1),(1,0),(-1,0)]
        q = [grid]
        cache[grid] = True

        while q:
            tmp = []

            for state in q:
                if state == goal:
                    return ans
                
                z = state.index("0")
                x,y = z//3, z%3

                for dx,dy in move:
                    nx, ny = x+dx, y+dy
                    
                    if 0<=nx<3 and 0<=ny<3:
                        ni = nx*3 + ny
                        ns = list(state)
                        ns[z],ns[ni] = ns[ni],ns[z]
                        ns = "".join(ns)

                        if cache.get(ns): continue
                        cache[ns] = True
                        tmp.append(ns)

            q = tmp
            ans += 1

        return -1

    for _ in range(3):
        grid += "".join(input().split())

    print(bfs())

if __name__ == "__main__":
    sys.exit(main())