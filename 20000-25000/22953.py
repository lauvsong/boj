import sys
input = sys.stdin.readline

def isPossible(mid):
    cnt = 0
    for a in A:
        cnt += mid // a

    return K <= cnt

def binarySearch():
    left, right = 1, 1e13

    while left <= right:
        mid = (left + right) // 2
        if isPossible(mid):
            right = mid - 1
        else:
            left = mid + 1

    return int(left)


def dfs(idx, cnt):
    global ans
    ans = min(ans, binarySearch())

    if cnt == C: return

    for i in range(idx, N):
        if 1 < A[i]:
            A[i] -= 1
            dfs(i, cnt+1)
            A[i] += 1

N,K,C = map(int, input().split())
A = list(map(int, input().split()))

ans = 1e13
dfs(0,0)

print(ans)

"""
22953. 도도의 음식 준비

n : 요리사 수 (1 <= n <= 10)
k : 음식 개수 (1 <= k <= 백만)
c : 격려 수
a : 음식 조리 시간 (1 <= a <= 백만)


# 1. 그리디 (x)
잘 모르겠음..


# 2. 완탐 (o)
구할 것 : 음식 조리 완료 최솟값

1. 요리사마다 가능한 격려를 모두 해보고

2. 조리 완료 시간 체크.

-> O(n! * K) ...?  개오바


# 설계
1. 격려 백트래킹.
2. 격려 합 C일 시 종료.
3. 종료 후 적용하여 조리 완료 시간 구함


# 조리 완료 시간 구하기 (이분탐색)

기준 : x 조리 완료 시간
check : x 시간 내 전부 처리 '가능한지' 확인.

    
"""