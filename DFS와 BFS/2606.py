def dfs(v) :
    global cnt
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            cnt += 1
            dfs(i)

def bfs(v):
    c = 0
    visit[v] = 1
    q = [v]
    while q:
        a = q.pop()
        for i in graph[a]:
            if visit[i] == 0:
                visit[i] = 1
                c += 1
                q.append(i)
    print(c)
a = int(input())
b = int(input())
graph = [[] * a for _ in range(a + 1)]
visit = [0] * (a + 1)
cnt = 0
for _ in range(b):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)
bfs(1)
# print(cnt)

# 각 포인트에서 연결된 위치만 확인하는 것이 중요