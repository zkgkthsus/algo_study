# 재귀 제한 때문에 아래 두줄은 필수
import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = True
    for i in check[v]:
        if not visit[i]:
            dfs(i)

m, n = map(int,input().split())
check = [[] for i in range(m + 1)]
visit = [False] * (m + 1)
cnt = 0


for i in range(n):
    y, x = map(int,input().split())
    check[y].append(x)
    check[x].append(y)

for j in range(1, m + 1):
    if not visit[j]:
        dfs(j)
        cnt += 1

print(cnt)
