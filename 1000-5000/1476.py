from itertools import cycle
import sys
input = sys.stdin.readline
#print = sys.stdout.write

target = tuple(map(int, input().split()))
e_cycle = cycle(range(1,16))
s_cycle = cycle(range(1,29))
m_cycle = cycle(range(1,20))

answer = 0
for esm in zip(e_cycle, s_cycle, m_cycle):
    answer += 1
    if esm == target:
        print(answer)
        break