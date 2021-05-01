# 다음 순열
import sys
input = sys.stdin.readline

def next_permutation(p):
    for i in range(n-1)[::-1]:
        if p[i] < p[i+1]:
            a = i
            break
    else:
        print(-1)
        sys.exit()

    for i in range(n)[::-1]:
        if p[i] > p[a]:
            b = i
            break

    p[a],p[b] = p[b],p[a]
    print(*(p[:a+1] + p[a+1:][::-1]))

n = int(input())
perm = list(map(int, input().split()))

next_permutation(perm)

# https://jins-dev.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%EC%B0%BE%EA%B8%B0-%EC%A0%84%EC%B2%B4-%EC%88%9C%EC%97%B4-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Next-Permutation