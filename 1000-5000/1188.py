from math import gcd
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
print(m - gcd(n,m))

"""
같은 양의 소시지를 주기 위해 최소 칼질 수

n : 소시지 개수
m : 음식 평론가 명수


이어붙인다고 가정.

최대공약수만큼 자르기
단, 애초에 배수일 때 -> 0
"""