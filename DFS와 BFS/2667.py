from collections import deque
a = int(input())
graph1 = [False] * a
graph2 = [[0] * a for _ in range(a)]
apart = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(y,x,c):
    if len(apart) < c:
        apart.append(1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= a or ny < 0 or ny >= a:
            continue
        if graph1[ny][nx] != '1':
            continue
        if graph2[ny][nx] != 0:
            continue
        graph2[ny][nx] = 1
        apart[c-1] += 1
        dfs(ny, nx, c)


for i in range(a):
    graph1[i] = list(input())
cnt = 0
for y in range(a):
    for x in range(a):
        if graph1[y][x] == '1' and graph2[y][x] == 0:
            cnt += 1
            graph2[y][x] = 1
            dfs(y,x,cnt)

# bfs를 구축해보았으나 실패
# cnt = 0
# for y in range(a):
#     for x in range(a):
#         if graph1[y][x] == '1' and graph2[y][x] == 0:
#             cnt += 1
#             q = deque()
#             q.append((y,x))
#             graph2[y][x] = 1
#             if len(apart) < cnt:
#                 apart.append(1)
#             while q:
#                 y,x = q.popleft()
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >= a or ny < 0 or ny >= a:
#                         continue
#                     if graph1[ny][nx] != '1':
#                         continue
#                     if graph2[ny][nx] != 0:
#                         continue
#                     apart[cnt-1] += 1
#                     graph2[ny][nx] = 1
#                     q.append((ny,nx))
print(len(apart))
for an in sorted(apart):
    print(an)