import sys
input = sys.stdin.readline

def initResult():
    res = 0

    for num in nums[:k]:
        if cache[num]  == 0:
            res += 1
        cache[num] += 1

    return res


def slide():
    ans = initResult()
    cnt = ans
    
    for i in range(0,n):
        if ans <= cnt:
            ans = cnt if cache[c] else cnt+1

        left = nums[i]
        right = nums[(i+k) % n]

        cache[left] -= 1

        if cache[left] == 0: cnt -= 1
        if cache[right] == 0: cnt += 1

        cache[right] += 1

    return ans

nums = []
n, d, k, c = map(int, input().split())
for _ in range(n):
    nums.append(int(input()))

cache = [0]*(d+1)

print(slide())

"""

# 문제
초밥 가짓수의 최댓값

# 조건
1. 임의의 위치부터 k개 연속 선택
2. 쿠폰 초밥 더하기



# 간략화
임의의 위치부터 k개 + 쿠폰초밥의 가짓수가 최대인 경우의 값을 구해라.

초밥 개수 : O(n^2) 불가.
접시 수 : O(n^2) 가능.

# 알고리즘
 
투 포인터. O(n)
"""