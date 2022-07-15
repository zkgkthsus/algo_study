import sys
input = sys.stdin.readline

a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for ans in b:
    print(ans)