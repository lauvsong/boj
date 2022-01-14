from collections import deque
import sys
input = sys.stdin.readline

def solve():
    q = deque([S])
    cache = [False]*(F+1)
    cache[S] = True
    result = 0

    while q:
        size = len(q)

        for _ in range(size):
            x = q.popleft()

            if x == G: return result

            for node in (x+U, x-D):
                if node < 1 or F < node: continue
                if cache[node]: continue
                q.append(node)
                cache[node] = True

        result += 1

    return "use the stairs"


F,S,G,U,D = map(int, input().split())
print(solve())


"""
F: 건물의 총 층수
G: 스타트링크의 위치
S: 강호 현재 위치

U: 위로 u층
D: 아래로 d층


* G층에 갈 수 없을 수 있음 -> "use the stairs"



---


BFS.


시작 : S

노드+U, 노드-D 큐잉
- 조건 1) 1층 미만일 경우 넘겨
- 조건 2) F층 초과일 경우 넘겨
"""