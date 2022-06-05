a = int(input())
b = [["*"] * a for _ in range(a)]

mc = int(a ** (1 / 3))


def recursion(i, j, cnt):
    global mc
    print("c:", (3 ** (cnt + 1)))
    # print("cnt:", cnt ,mc)
    if cnt == mc:
        return
    c, d = i // (3 ** cnt), j // (3 ** cnt)
    e, f = c % 3, d % 3
    if e == 1 and f == 1:
        b[i][j] = " "
    if c > 3 or d > 3:
        recursion(i, j, cnt + 1)


for i in range(a):
    for j in range(a):
        recursion(i, j, 0)

for bc in b:
    print(*bc)
