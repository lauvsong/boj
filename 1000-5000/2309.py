import sys
input = sys.stdin.readline

def findSpy():
    for x in range(9):
        for y in range(x+1, 9):
            result = heights[x] + heights[y]
            if result == offset: return heights[x], heights[y]

heights = [int(input().strip()) for _ in range(9)]
offset = sum(heights) - 100

spy1, spy2 = findSpy()
heights.sort()

for index, height in enumerate(heights):
    if height == spy1 or height == spy2: continue
    print(height)