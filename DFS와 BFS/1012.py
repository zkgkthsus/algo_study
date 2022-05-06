import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    global asd
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= a or ny < 0 or ny >= b:
            continue
        if graph[ny][nx] == 1 and graph2[ny][nx] == 0:
            graph2[ny][nx] = 1
            dfs(ny, nx)

earth = int(input())


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(earth):
    asd = 0
    a, b, c = map(int, input().split())
    graph = [[0] * a for _ in range(b)]
    graph2 = [[0] * a for _ in range(b)]
    cnt = 0
    for _ in range(c):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1 and graph2[i][j] == 0:
                cnt += 1
                graph2[i][j] = 1
                dfs(i, j)
    print(cnt)
# dfs로 풀때 1,2줄의 코드가 없으면 런타임 에러가 발생한다
# 문제에서 가로 세로인한 최대 면적은 2500 인데 런타임 에러가 발생한다는 것은
# 백준에는 기본적으로 2500이하의 반복회수를 허용하는 것 같다.