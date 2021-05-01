import sys
input = sys.stdin.readline

def main():

    def bfs(n,k):
        q = [n]
        cache = [False]*100001
        parent = [0]*100001
        cnt = 0
        route = [k]

        while q:
            tmp = []

            for x in q:
                if x == k: break

                for i in (x-1, x+1, x*2):
                    if 0 <= i < 100001 and not cache[i]: 
                        cache[i] = True
                        parent[i] = x
                        tmp.append(i)
            
            q = tmp

        while k != n:
            route.append(parent[k])
            k = parent[k]
        
        print(len(route)-1)
        print(*route[::-1])

    n,k = map(int, input().split())
    bfs(n,k)


if __name__ == "__main__":
    sys.exit(main())