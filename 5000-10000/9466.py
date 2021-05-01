import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cache = [0]*n
        ans = n
        group = 0

        students = list(map(int, input().split()))
        for s in range(len(students)):
            if cache[s] == 0:
                group += 1
                while not cache[s]:
                    cache[s] = group
                    s = students[s]-1

                while cache[s] == group:
                    cache[s] = -1
                    s = students[s]-1
                    ans -= 1

        print(ans)

if __name__ == "__main__":
    sys.exit(main())