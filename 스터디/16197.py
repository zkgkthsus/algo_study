from collections import deque
from copy import deepcopy

n, m = map(int,input().split())
array = [ list(input()) for _ in range(n)]
c1 = ''
c2 = ''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Ccnt = 0
for y in range(n):
    for x in range(m):
        if array[y][x] == 'o':
            if c1 == '':
                c1 = [y, x]
            else:
                c2 = [y, x]
point = c1 + c2

def dfs(array, y, x, d, c):   
    global Ccnt, p
    
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        Ccnt += 1
        return array
    if array[ny][nx] == 'o' or array[ny][nx] == '#':
        print('코인',c)
        Ccnt += 1
        return array
    array[y][x] = '.'
    array[ny][nx] = 'o'
    if c == 0:
        p[0],p[1] = ny, nx
    else:
        p[2],p[3] = ny, nx
    return deepcopy(array)
    
    

# 상,하,좌,우
def first(array, d):
    if d == 0:
        if array[0] > array[2]:
            array[0], array[1], array[2], array[3] = array[2], array[3], array[0], array[1]
    elif d == 1:
        if array[0] < array[2]:
            array[0], array[1], array[2], array[3] = array[2], array[3], array[0], array[1]
    elif d == 2:
        if array[1] > array[3]:
            array[0], array[1], array[2], array[3] = array[2], array[3], array[0], array[1]
    elif d == 3:
        if array[1] < array[3]:
            array[0], array[1], array[2], array[3] = array[2], array[3], array[0], array[1]
    
    return array

array2 = deepcopy(array)
q = deque([[point, array2, 0]])
# print(q)
while q:
    a = q.popleft()
    # print(a)
    p, dm, c = a[0], a[1], a[2]
    print('!',p,dm,c)
    if c > 4:
        break
    for i in range(4):
        Ccnt = 0
        p = first(p, i)
        dm1 = dfs(dm, p[0], p[1], i, 0)
        dm2 = dfs(dm1, p[2], p[3], i, 1)
        # nx1 = p[0] + dx[i]
        # ny1 = p[1] + dy[i]
        # nx2 = p[2] + dx[i]
        # ny2 = p[3] + dy[i]
        # if nx1 < 0 or nx1 >= m or ny1 < 0 or ny1 >= n:
        #     Ccnt += 1
        # if array[ny1][nx1] == 'o' or array[ny1][nx1] == '#':
        # array[y][x] = '.'
        # array[ny][nx] = 'o'
        # if nx < 0 or nx >= m or ny < 0 or ny >= n:
        #     Ccnt += 1
        # if array[ny][nx] == 'o' or array[ny][nx] == '#':
        print("!!!", Ccnt, i)
        if Ccnt == 1:
            print('!!',c + 1)
            exit()
        elif Ccnt == 0:
            q.append([p[:], dm2, c + 1])
print(-1)



    