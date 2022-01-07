import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1: continue
            if g[i][k] + g[k][j] != 2: continue
            g[i][j] = 1


for i in range(n):
    print(" ".join(str(line) for line in g[i]))

"""
# 문제
G : 가중치X 그래프
i->j 경로 유무 판단

# 입력
N : 정점의 개수


간선들 정보는 주어짐.
모든 정점 쌍에 대하여 -> 경로 유무 판단


# 알고리즘
플로이드 워셜.

워셜 수행 후
값이 초기화 상태 시 0
변화했으면 1


# 반복문
모든 정점 k
    시작점 i
        끝점 j
            if dp[i,j] != 0: continue
            if dp[i,k] * dp[k,j] == 0: continue
            dp[i,j] = 1

"""