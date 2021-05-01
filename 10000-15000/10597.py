import sys
input = sys.stdin.readline

def main():
    def solve(idx):
        if idx == ln:
            print(*ans)
            sys.exit()

        num = ""
        for i in range(idx, idx+2):
            if i >= ln: continue
            num = num + perm[i]

            if (inum := int(num)) > n: continue
            if cache[inum]: continue

            cache[inum] = True
            ans.append(inum)
            solve(i+1)
            cache[inum] = False
            ans.pop()

    perm, ans = input().rstrip(), []
    ln = len(perm)
    n = 9 + (ln-9)//2
    cache = [False]*(n+1)
    solve(0)

if __name__ == "__main__":
    sys.exit(main())