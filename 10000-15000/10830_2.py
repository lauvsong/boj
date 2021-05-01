import numpy as np
import sys
input = sys.stdin.readline
#print = sys.stdout.write

n,b = map(int, input().split())
frame = [list(map(int, input().split())) for _ in range(n)]
frame = np.array(frame).reshape(n,n)
naive = frame.copy()

for _ in range(b-1):
    frame = np.dot(frame, naive)
    
frame = frame % 1000
for i in frame:
    print(*i)