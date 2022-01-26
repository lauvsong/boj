import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x

    parent[x] = find(parent[x])
    return parent[x]

def isCycle(a,b):
    x = find(a)
    y = find(b)

    if x == y: return True
    if x < y: parent[y] = x
    else: parent[x] = y

    return False

def solve():
    result = 0

    for i in range(m):
        a,b = map(int, input().split())
        if isCycle(a,b): 
            result = i+1
            break
    
    return result

n,m = map(int, input().split())
parent = [i for i in range(n)]

print(solve())


"""
20040. 사이클 게임

# 문제
몇번째 차례에서 사이클이 완성됐는지 (미종료 시 0)

n : 점의 개수 (3 <= n <= 500000)
m : 진행된 차례  (3 <= m <= 1000000)


매 입력마다 유니온 파인드.

"""