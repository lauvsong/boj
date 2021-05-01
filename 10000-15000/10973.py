# 이전 순열
import sys
input = sys.stdin.readline

def next_permutation(p):
    for i in range(n-1)[::-1]:
        if p[i] > p[i+1]:
            a = i
            break
    else:
        print(-1)
        sys.exit()

    for i in range(n)[::-1]:
        if p[i] < p[a]:
            b = i
            break

    p[a],p[b] = p[b],p[a]
    print(*(p[:a+1] + p[a+1:][::-1]))

n = int(input())
perm = list(map(int, input().split()))
next_permutation(perm)