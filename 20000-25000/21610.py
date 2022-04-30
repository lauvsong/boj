from copy import deepcopy

CLOUD = 1
DISAPPEARED = 2

N, M = map(int, input().split())
bucket = []
clouds = [[0] * N for _ in range(N)]
directions = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

cache = []

def init():
    cache.clear()

def cast():
    clouds[N - 1][0] = CLOUD
    clouds[N - 1][1] = CLOUD
    clouds[N - 2][0] = CLOUD
    clouds[N - 2][1] = CLOUD


def move_clouds(d, s):
    for x in range(N):
        for y in range(N):
            if clouds[x][y] != CLOUD: continue
            clouds[x][y] = 0
            move(x, y, d, s)

    for x,y in cache:
        clouds[x][y] = DISAPPEARED

    bug()
    last()


def move(x, y, d, s):
    for _ in range(s):
        nx, ny = get_newxy(x, y, d)
        x = nx
        y = ny

    bucket[x][y] += 1
    cache.append((x, y))


def get_newxy(x, y, d):
    dx, dy = directions[d]
    nx = x + dx
    ny = y + dy

    return circle_num(nx), circle_num(ny)


def circle_num(x):
    if x == -1:
        return N - 1
    elif x == N:
        return 0

    return x


def bug():
    global bucket
    dirs4 = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    tmp = deepcopy(bucket)

    for x,y in cache:
        for dx, dy in dirs4:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if bucket[nx][ny] == 0: continue
                tmp[x][y] += 1

    bucket = tmp

def last():
    for x in range(N):
        for y in range(N):
            if clouds[x][y] == DISAPPEARED:
                clouds[x][y] = 0
                continue
            if bucket[x][y] < 2: continue

            clouds[x][y] = CLOUD
            bucket[x][y] = bucket[x][y] - 2

def get_answer():
    return sum(sum(x) for x in bucket)

for _ in range(N):
    bucket.append(list(map(int, input().split())))

cast()
for _ in range(M):
    d, s = map(int, input().split())
    init()
    move_clouds(d - 1, s)

print(get_answer())