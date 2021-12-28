import sys
input = sys.stdin.readline

def solve(x):
    if x < 2: return 2

    while not isAnswer(x):
        x += 1
    return x

def isAnswer(x):
    if not isPalindrome(x): return False
    if not isPrime(x): return False

    return True

def isPalindrome(x):
    if x % 10 == 0: return False

    revertedNumber = 0
    while x > revertedNumber:
        quotient, remainder = divmod(x, 10)
        revertedNumber = revertedNumber * 10 + remainder
        x = quotient
    
    return x == revertedNumber or x == revertedNumber//10

def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return False
    return True

n = int(input())
print(solve(n))


"""
# 소수 & 팰린드롬

range: N <= answer (소수, 팰린드롬)

완전탐색
    조건 1. 소수
    조건 2. 팰린드롬

O(nlogn) 예상.
"""