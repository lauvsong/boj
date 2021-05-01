import sys
input = sys.stdin.readline

def main():
    def bfs():
        q = [0]
        cache = [0]*n
        cache[0] = 1
        
        while q:
            tmp = []

            for x in q:
                for i in tree[x]:
                    if cache[i]: continue
                    cache[i] = x+1
                    tmp.append(i)

            q = tmp

        print(*cache[1:], sep='\n')

    n = int(input())
    tree = [[] for _ in range(n)]

    for _ in range(n-1):
        a,b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    bfs()

if __name__ == "__main__":
    sys.exit(main())