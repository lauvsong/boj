import sys
input = sys.stdin.readline

def dynamic(n):
    arr = [1,2,4]
    for i in range(3,n):
        arr.append(sum(arr[-3:]))
    return arr[n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dynamic(n))