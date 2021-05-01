import sys
input = sys.stdin.readline

def main():
    def bfs(n,k):
        q = [n]
        cache = [[False]*500001 for _ in range(2)]
        cache[0][n] = True
        flag = 0
        level = 0

        while q:
            if k > 500000: break
            if cache[flag][k]: return level

            tmp = []
            flag = 1 - flag
            for x in q:
                for i in (x-1, x+1, x*2):
                    if 0 <= i <= 500000 and not cache[flag][i]:
                        cache[flag][i] = True
                        tmp.append(i)
            
            level += 1
            k += level
            q = tmp

        return -1
    
    n,k = map(int, input().split())
    print(bfs(n,k))

if __name__ == "__main__":
    sys.exit(main())