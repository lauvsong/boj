import sys
input = sys.stdin.readline

s = int(input())
cache = {}

def copyAll(q, node):
    if cache.get((node, node)): return
    cache[(node, node)] = True
    q.append((node, node))

def paste(q, node, clip):
    result = node + clip
    if cache.get((result, clip)): return
    cache[(result, clip)] = True
    q.append((result, clip))

def deleteOne(q, node, clip):
    result = node - 1
    if cache.get((result, clip)): return
    cache[(result, clip)] = True
    q.append((result, clip))


def bfs(start, end):
    q = [(start, 0)]
    cache[(start, 0)] = True
    result = 0

    while q:
        tmp = []

        for node, clip in q:
            if node == end: return result

            copyAll(tmp, node)
            paste(tmp, node, clip)
            deleteOne(tmp, node, clip)

        q = tmp
        result += 1

print(bfs(1,s))



"""
이모티콘을 S개 만들기 위한 시간의 최소값

작업 (각각 1초)
1. 전체 복사
2. 붙여넣기
3. 1개 삭제

S : 이모티콘 개수 (2 <= S <= 100)

초기화 상태 : 이모티콘 1개.

---

BFS

시작: 1
종료: S

작업 3개 적용 노드.

cache = 클립보드 이모지 수
**False는 미방문.

"""