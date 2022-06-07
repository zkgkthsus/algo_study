a = int(input())
L = [i for i in range(a, 1, -1)]
C = []
R = []
pro = []


def recursion(L, C, R):
    if len(L) > 0:
        if len(C) == 0:
            C.append(L.pop())


if a % 2 == 1:
    pro.append([1, 3])
    R.append(1)
elif a % 2 == 0:
    pro.append([1, 2])
    C.append(1)
