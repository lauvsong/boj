import sys
input = sys.stdin.readline

k = int(input())
sign = input().split()
cache = [False]*10
mini, maxi = "9999999", ""

def solve(idx, ans):
    global mini, maxi
    if idx == k+1:
        if mini > ans: mini = ans
        elif maxi < ans: maxi = ans
        return

    for i in range(10):
        if cache[i]: continue
        if idx == 0 or eval(f'{ans[-1]}{sign[idx-1]}{i}'):
            cache[i] = True
            solve(idx+1, ans+str(i))
            cache[i] = False


solve(0,"")
print(maxi)
print(mini)