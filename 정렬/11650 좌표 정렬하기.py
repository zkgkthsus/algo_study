import sys
input = sys.stdin.readline

a = int(input())
b = []
for i in range(a):
    b.append(list(map(int,input().split())))
b.sort(key= lambda x : (x[0],x[1]))
for i in range(a):
    print(*b[i])
