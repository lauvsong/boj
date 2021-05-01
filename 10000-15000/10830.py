import sys
input = sys.stdin.readline
#print = sys.stdout.write

def matrix(n, frame1, frame2):
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                answer[i][j] += frame1[i][k]*frame2[k][j]
            answer[i][j] %= 1000
    return answer

n,b = map(int, input().split())
naive = [list(map(int, input().split())) for _ in range(n)]
frame = naive.copy()
binary = str(bin(b))
if b == 1:
    for f in frame:
        print(*list(map(lambda x: x%1000, f)))
else:
    for b in binary[3:]:
        frame = matrix(n, frame, frame)
        if b == "1": frame = matrix(n, frame, naive)

    for f in frame:
        print(*f)