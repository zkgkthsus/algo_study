import sys

input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b.append(list(input().split()))

b.sort(key=lambda a: int(a[0]))

for i in range(a):
    print(b[i][0], b[i][1])
