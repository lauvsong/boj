import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
rates = defaultdict(int)

def setRatesMap(word):
    x = 1
    for letter in word[::-1]:
        rates[letter] += x
        x *= 10

def getAnswer():
    result = 0
    x = 9
    sortedMap = sorted(rates.items(), key=lambda x: x[1], reverse=True)
    for _, value in sortedMap:
        result += x * value
        x -= 1

    return result

for _ in range(n):
    word = input().strip()
    setRatesMap(word)

print(getAnswer())

"""
알파벳마다 딕셔너리. 비율 숫자로 표기
"""