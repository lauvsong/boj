import sys

input = sys.stdin.readline

n = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

counts = [0]*n

def serveBox(box):
    candidate = 0

    for i, crane in enumerate(cranes):
        if crane < box: break
        if box <= crane and counts[i] < counts[candidate]:
            candidate = i
    
    counts[candidate] += 1


def solve():
    if cranes[0] < boxes[0]: return -1

    for box in boxes:
        serveBox(box)

    return max(counts)

print(solve())


"""

모든 박스를 배로 옮기는데 드는 최소 시간.
1분에 박스 하나.

N: 크레인의 수 (<= 50)
M: 박스의 수 (<=10000)

크레인 무게제한 (<=1000000)
박스 무게 (<=1000000)


**
모든 박스 처리 불가능한 경우 존재. -> -1 출력


1. 무게제한 큰 크레인이 항상 가장 큰 박스를 가져가도록 함.
-> 예외 : x. (Greedy 가능)

2. 가장 큰 크레인 무게제한보다 박스 무게가 더 큰 경우 -> 불가능. (-1 출력)

박스에게 최적의 크레인 배정.


"""
