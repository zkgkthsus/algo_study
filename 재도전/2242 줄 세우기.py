from collections import deque

n, m = map(int,input().split())
# 각 정점과 연결된 노드 기록
graph = [[] for _ in range(n + 1)]
# 몇 번이나 순서에 대한 규칙이 존재하는가
inDegree = [0 for _ in range(n + 1)]
q = deque()
ans = []

for i in range(m):
    a, b = map(int,input().split())
    # a기준으로 b보다 앞에 있다
    graph[a].append(b)
    # b 앞에는 기록된 숫자만큼 존재한다
    inDegree[b] += 1

for i in range(1, n + 1):
    # 만약 순서 규칙이 존재하지 않으면 먼저 배치
    if inDegree[i] == 0:
        q.append(i)
# 1차 순서가 정해지면 순서가 다 정해질때 까지 반복
while q:
    # 여기서 나오는 순서는 제일 먼저 나올 수 있다
    tmp = q.popleft()
    # 나온 순서는 정답에 기록
    ans.append(tmp)
    # 순서에 대한 규칙이 정해져 있으면 아래 반복문 실행
    for i in graph[tmp]:
        # 앞에 순서가 고정 되었으니 1씩 당겨준다
        inDegree[i] -= 1
        # 남은 숫자가 없으면 1차순서표에 넣어준다.
        if inDegree[i] == 0:
            q.append(i)
print(*ans)