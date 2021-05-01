import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
A, B, C, D = [], [], [], []
answer = 0

for _ in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

hash_table = {}
for a in A:
    for b in B:
        part = a + b
        try: hash_table[part] += 1
        except: hash_table[part] = 1

for c in C:
    for d in D:
        try: answer += hash_table[-(c+d)]
        except: continue

print("%d" % answer)