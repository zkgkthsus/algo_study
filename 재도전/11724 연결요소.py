m, n = map(int,input().split())
check = [i for i in range(1, m + 1)]
def team_set(y, x):
    if y > x:
        for i in range(m):
            if (x - 1) != i and check[i] == check[y - 1]:
                team_change(i, x)
    elif y < x:
        for i in range(m):
            if (y - 1) != i and check[i] == check[x - 1]:
                team_change(i, y)

def team_change(i, y):
    check[i] = check[y - 1]

for i in range(n):
    y, x = map(int,input().split())
    team_set(y,x)
check = set(check)
print(len(check))