import sys
input = sys.stdin.readline

def main():
    def bfs():
        q = [n]
        cache = [False]*100001
        ans = 0

        while q:
            tmp = []

            for x in q:
                if x == k: return ans

                for i in (x-1, x+1, x*2):
                    if 0 <= i < 100001 and not cache[i]: 
                        cache[i] = True
                        tmp.append(i)
            
            q = tmp
            ans += 1

    n,k = map(int, input().split())
    print(bfs())

if __name__ == "__main__":
    sys.exit(main())