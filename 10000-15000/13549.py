import sys
input = sys.stdin.readline

def main():

    def bfs(n,k):
        q = [(0,n)]
        cache = [False]*100001

        while q:
            tmp = []

            for cnt,x in q:
                if x == k: return cnt

                if x*2 <= 100000 and not cache[x*2]: 
                    cache[x*2] = True
                    tmp.append((cnt,x*2))
                if 0 <= x-1 and not cache[x-1]: 
                    cache[x-1] = True
                    tmp.append((cnt+1,x-1))
                if x+1 <= 100000 and not cache[x+1]: 
                    cache[x+1] = True
                    tmp.append((cnt+1,x+1))
                
            q = tmp

    n,k = map(int, input().split())
    print(bfs(n,k))


if __name__ == "__main__":
    sys.exit(main())