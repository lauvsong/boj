import sys
input = sys.stdin.readline

n = int(input())
honeys = list(map(int, input().split()))

sums = honeys[:]
ans = 0

for i in range(1,n):
    sums[i] += sums[i-1]

for i in range(1, n-1):
    ans = max(ans, 2*sums[-1] - honeys[0] - honeys[i] - sums[i])
for i in range(1, n-1):
    ans = max(ans, sums[-1] - honeys[-1] - honeys[i] + sums[i-1])
for i in range(1, n-1):
    ans = max(ans, sums[i] - honeys[0] + sums[-1] - sums[i-1] - honeys[-1])

print(ans)

"""
꿀 따기

# 문제
벌(2)과 벌통(1)을 임의 배치하여, 최대 꿀 양을 구해라.

# 변수
N : 장소의 수 (3 <= N <= 십만)


케이스
1. 벌통이 벌 사이에 있음
- 벌이 무조건 양 끝에 있어야 함.

2. 벌통이 왼쪽, 오른쪽 끝에 있음
- 하나는 반대쪽 끝에 있어야 함.
- 하나는 완탐


# 알고리즘
누적합

"""