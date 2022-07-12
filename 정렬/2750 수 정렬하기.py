a = int(input())
b = [int(input()) for _ in range(a)]
b.sort()
for c in b:
    print(c)