import sys
input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())
i = 2

while n != 1:
    q, r = divmod(n,i)
    if r == 0:
        n = q
        print(i)
    else:
        i += 1