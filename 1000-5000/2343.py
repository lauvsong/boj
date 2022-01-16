import sys
input = sys.stdin.readline        

def check(mid):
    res = size = 0

    for bluray in blurays:
        size += bluray
        if mid <= size:
            res += 1
            size = bluray if mid < size else 0

    if size: res += 1

    return res

def binarySearch():
    left, right = max(blurays), sum(blurays)

    while left <= right:
        mid = (left + right) // 2
        if m < check(mid): left = mid+1
        else: right = mid-1

    return left


n,m = map(int, input().split())
blurays = list(map(int, input().split()))

print(binarySearch())

"""
# 기타 레슨

m개의 블루레이의 크기가 모두 같아야 하고,
블루레이 크기 최솟값.

*순서 유지.
*꼭 크기에 꽉 채울 필요는 없음.

강의 길이 <= 10000
1 <= n <= 100000
1 <= m <= n

---

디피 X.
그리디 애매.

완탐 O(n^2) = 1억 X (불가능)
- res = 처음부터 더하기
- res 값으로 원소 나누기

- 블루레이 총 개수가 m이면 ok.
- 아니면 다시 완탐.


이분탐색 선정.

탐색
- 매개변수: param (블루레이 최소 크기 후보)

# 반복문
ans : 블루레이 개수

전체 (n)
- res: 더하기.
- 조건 1) param <= res -> res = i, ans += 1

return ans

"""