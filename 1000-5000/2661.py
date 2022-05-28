import sys
input = sys.stdin.readline

def is_good(num):
    n = len(num)

    for i in range(1, n // 2 + 1):
        if num[-(i*2):-i] == num[-i:]:
            return False
    
    return True


def dfs(num):
    if len(num) == N:
        print(num)
        exit()

    for i in '123':
        next_num = num + str(i)
        if is_good(next_num):
            dfs(next_num)


N = int(input())
dfs('1')

"""
# 문제
길이가 N인 '좋은' 수열 중 가장 '작은' 수 
N (<=80)


인접한 두개의 부분 수열이 동일하면 안됨.

1. 완탐
1, 1
2, 2
3, 3 
/...

1213

n = 현재길이
for 1 ~ :
    for 1 ~ n:
        if 나쁜수열: break

1. 1부터 숫자 늘려감
2. -1번째부터 n // 2까지 숫자 비교함
    if 같을 시: break (나쁜수열)
3. 

def run():
    num = 0
    ans.append(num)
    while True:
        ans[-1] += 1
        curr = len(ans)-1
        for gap in range(1, n//2):
            if ans[curr-gap*2:curr-gap] == if ans[curr-gap:curr]



for _ in range(N):
    run()
"""