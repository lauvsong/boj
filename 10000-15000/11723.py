import sys
input = sys.stdin.readline
print = sys.stdout.write

s = 0
for _ in range(int(input())):
    op, *num = input().split()
    if num: i = int(num[0])-1

    if op == "add": s |= 1 << i
    elif op == "remove": s &= ~(1 << i)
    elif op == "check": print('1\n' if s & (1 << i) else '0\n')
    elif op == "toggle": s ^= 1 << i
    elif op == "all": s = (1 << 20) - 1
    else: s = 0