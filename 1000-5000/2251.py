import sys
input = sys.stdin.readline

def main():
    def bfs(a,b,c):

        def caching(a,b,c):
            if not cache[a][b]:
                cache[a][b] = True
                tmp.append((a,b,c))

        q = [(0,0,c)]
        cache = [[False]*(b+1) for _ in range(a+1)]
        cache[0][0] = True
        ans = []

        while q:
            tmp = []
            for x,y,z in q:

                if x == 0: ans.append(z)
                if x+y <= b: 
                    caching(0,x+y,z)
                else: 
                    gap = b-y
                    caching(x-gap, b, z)

                if x+y <= a: 
                    caching(x+y,0,z)
                else:
                    gap = a-x
                    caching(a, y-gap, z)

                if x+z <= c: 
                    caching(0,y,x+z)
                else:
                    gap = c-z
                    caching(x-gap, y, c)

                if x+z <= a: 
                    caching(x+z,y,0)
                else:
                    gap = a-x
                    caching(a,y,z-gap)

                if y+z <= b: 
                    caching(x,y+z,0)
                else:
                    gap = b-y
                    caching(x,b,z-gap)

                if y+z <= c: 
                    caching(x,0,y+z)
                else:
                    gap = c-z
                    caching(x, y-gap, c)

            q = tmp
        return ans

    a,b,c = map(int, input().split())
    print(*sorted(bfs(a,b,c)))

if __name__ == "__main__":
    sys.exit(main())