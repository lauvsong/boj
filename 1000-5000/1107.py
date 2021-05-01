import sys
input = sys.stdin.readline
#print = sys.stdout.write

N = int(input())
M = int(input())

gap = abs(N-100)
if gap <= 2:
    if M != 0: input()
    print(gap)
    sys.exit(0)

if not M:
    print(len(str(N)))
    sys.exit(0)

buttons = set(map(str, range(0,10))) - set(input().split())   
if not buttons:
    print(gap)
    sys.exit(0)

up, down = 1000000, 1000000
for num in range(N, 1000001):
    for i in str(num):
        if i not in buttons: break
    else:
        up = num
        break
    
for num in range(N, -1, -1):
    for i in str(num):
        if i not in buttons: break
    else: 
        down = num
        break

closest = up if abs(up-N) < abs(down-N) else down
print(min(len(str(closest)) + abs(closest-N), gap))