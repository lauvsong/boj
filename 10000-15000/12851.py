import sys
input = sys.stdin.readline

def main():

    def bfs(n,k):
        q = [n]
        cache = [False]*100001
        cnt = 0

        while q:
            tmp = []

            for x in q:
                if x == k:
                    print(cnt, q.count(k), sep="\n")
                    return

                cache[x] = True
                for i in (x-1, x+1, x*2):
                    if 0 <= i < 100001 and not cache[i]: tmp.append(i)
            
            q = tmp
            cnt += 1

    n,k = map(int, input().split())
    bfs(n,k)


if __name__ == "__main__":
    sys.exit(main())