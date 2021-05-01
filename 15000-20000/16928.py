import sys
input = sys.stdin.readline

def main():
    board = [0]*100
    n,m = map(int, input().split())

    for _ in range(n+m):
        x,y = map(int, input().split())
        board[x-1] = y-1

    q = [0]
    cache = [False]*100
    cache[0] = True
    cnt = 0

    while q:
        tmp = []

        for i in q:
            if i == 99:
                print(cnt)
                sys.exit()

            for loc in range(i+1,i+7):
                if loc >= 100: continue

                if board[loc]:
                    if cache[board[loc]]: continue
                    tmp.append(board[loc])
                    cache[board[loc]] = True
                elif not cache[loc]:
                    tmp.append(loc)
                    cache[loc] = True

        q = tmp
        cnt += 1

if __name__ == "__main__":
    sys.exit(main())