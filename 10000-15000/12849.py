import sys
input = sys.stdin.readline

# 노가다 함수
def go(tmp):
    dp[0] = tmp[1] + tmp[2] # 정보과학
    dp[1] = tmp[0] + tmp[2] + tmp[3]  # 전산
    dp[2] = tmp[0] + tmp[1] + tmp[3] + tmp[5] # 미래
    dp[3] = tmp[1] + tmp[2] + tmp[4] + tmp[5] # 신양
    dp[4] = tmp[3] + tmp[5] + tmp[6] # 진리
    dp[5] = tmp[2] + tmp[3] + tmp[4] + tmp[7] # 한경
    dp[6] = tmp[4] + tmp[7] # 학생회
    dp[7] = tmp[5] + tmp[6] # 형남

D = int(input())
dp = [0]*8
dp[0] = 1

for i in range(1,D+1):
    go(dp[:])

print(dp[0] % 1000000007)

"""
# 본대 산책

BFS 하고싶다

## 배열
dp[n][i] : n초 후 i 건물로 가는 경우의 수

## 점화식
dp[n][i] = dp[n-1][인접] + .. 인접한 애들 다 더하기 .. ?? 노가다??

# 인덱스
0: 정보과학
1: 전산
2: 미래
3: 신양
4: 진리
5: 한경
6: 학생회
7; 형남
"""