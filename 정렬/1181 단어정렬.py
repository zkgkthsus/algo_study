import sys
input = sys.stdin.readline
a = int(input())
b = [[] for i in range(51)]
for i in range(a):
    c = input().strip()
    if c not in b[len(c)]:
        b[len(c)].append(c)
# print(b)
for j in range(1,51):
    if len(b[j]) > 0:
        b[j].sort()
        for ans in b[j]:
            print(ans)