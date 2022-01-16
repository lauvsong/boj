import sys
input = sys.stdin.readline

def check(mid):
    res = 0
    for time in t:
        res += mid // time

    return m <= res

def binarySearch():
    left, right = 1, max(t)*m
import sys
input = sys.stdin.readline

def check(mid):
    res = 0
    for time in t:
        res += mid // time

    return m <= res

def binarySearch():
    left, right = 1, max(t)*m

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid-1
        else:
            left = mid + 1
    
    return left
    

n,m = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))

print(binarySearch())

"""
3079. 입국심사

n : 입국심사대 개수
m : 사람 수

# 문제
모두 심사를 받는데 걸리는 시간의 최솟값

# 1. 그리디 (기각)
각 심사대 마다
남은 초 수 + 심사 시간을 구함.
가장 적게 남은 심사대로 가게 함.
-> 매 사람 마다 반복

O(m * n) 10억 * 10만..? 오반데

선형 탐색하지 않고 우선순위 큐를 이용한다면 -> 그래도 O(nlogn)

:O(n)을 넘으면 안되므로 기각


# 2. 이분탐색 (채택)
기준 : 심사에 걸리는 시간
최소 : 1
최대 : max(심사대) * 사람 수


# check 함수
- m명 심사가 가능한지 판단.


"""