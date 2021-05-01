import sys
input = sys.stdin.readline
#print = sys.stdout.write

def func(pre):
    global ans
    if len(stack) <= 2:
        ans = max(ans, pre)
        return 
    else:
        for i in range(1, len(stack) - 1):
            res = stack[i-1]*stack[i+1]
            node = stack[i]
            del stack[i]
            func(pre + res)
            stack.insert(i, node)

n = int(input())
stack = list(map(int, input().split()))
ans = 0

func(0)
print(ans)