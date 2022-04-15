alist = [-1] * 26
a = input()
cnt = 0
for i in a:
    b = ord(i) - 97
    if alist[b] == -1:
        alist[b] = cnt
    cnt += 1
print(*alist)