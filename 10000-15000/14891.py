import sys
input = sys.stdin.readline

def getResult():
    result = 0
    scores = tuple((1,2,4,8))

    for gear, score in zip(gears, scores):
        if gear & (1 << 7): 
            result += score

    return result

def setLeftDirection(gear, directions):
    for i in reversed(range(1, gear+1)):
        left = right = 'N'
        if gears[i-1] & (1 << 5): left = 'S'
        if gears[i] & (1 << 1): right = 'S'

        if left == right: break
        directions[i-1] = -directions[i]

def setRightDirection(gear, directions):
    for i in range(gear, 3):
        left = right = 'N'
        if gears[i] & (1 << 5): left = 'S'
        if gears[i+1] & (1 << 1): right = 'S'

        if left == right: break
        directions[i+1] = -directions[i]

def rotate(directions):
    for i in range(4):
        if directions[i] == 1:
            lastBit = True if gears[i] & 1 else False
            gears[i] >>= 1
            if lastBit:
                gears[i] |= (1 << 7)
        
        if directions[i] == -1:
            firstBit = True if gears[i] & (1 << 7) else False
            gears[i] <<= 1
            if firstBit:
                gears[i] &= ~(1 << 8)
                gears[i] += 1

def roll(gear, direction):
    directions = [0]*4
    directions[gear] = direction

    setLeftDirection(gear, directions)
    setRightDirection(gear, directions)
    rotate(directions)

gears = [int(input(), 2) for _ in range(4)]

k = int(input())
for _ in range(k):
    gear, direction = map(int, input().split())
    roll(gear-1, direction)

print(getResult())


"""
14891. 톱니바퀴

최종 톱니바퀴의 상태를 구하는 프로그램

---

# 출력
12시 방향 N/S 여부

# roll
1. 현재 상태 탐색 후 톱니바퀴 별 방향 설정.
2. 방향 대로 shift

선택된 gear 주변으로 반복문 전파.

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
"""