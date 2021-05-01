import sys
input = sys.stdin.readline
print = sys.stdout.write

sieve = set(range(2,1000001))
for i in range(2, 1001):
    sieve -= set(range(i*2, 1000001, i))

nums = []
n = int(input())
while n:
    for i in sieve:
        x,y = i, n-i
        if x > n//2: break
        if set({y}) & sieve:
            print("{} = {} + {}\n".format(n, x, y))
            break
    else:
        print("Goldbach's conjecture is wrong.")
    n = int(input())