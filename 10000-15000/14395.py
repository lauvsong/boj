import sys
input = sys.stdin.readline

def main():
    def bfs(s,t):
        if s == t: return 0
        bound = 10e9
        cache = {s}
        q = [(s, "")]
        cnt = 0

        while q:
            tmp = []

            for i,hist in q:
                if i == t: return hist

                if (op := i*i) <= bound and not set({op}) & cache: 
                    tmp.append((op, hist+"*"))
                    cache.add(op)

                if (op := i+i) <= bound and not set({op}) & cache: 
                    tmp.append((op, hist+"+"))
                    cache.add(op)

                if not set({op := 0}) & cache: 
                    tmp.append((op, hist+"-"))
                    cache.add(op)

                if not set({op := 1}) & cache:
                    tmp.append((op, hist+"/"))
                    cache.add(op)
            
            cnt += 1
            q = tmp

        return -1


    s,t = map(int, input().split())
    print(bfs(s,t))

if __name__ == "__main__":
    sys.exit(main())