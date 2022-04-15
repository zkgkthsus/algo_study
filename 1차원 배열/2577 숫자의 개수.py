cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = int(input())
b = int(input())
c = int(input())
ans = str(a * b * c)
for i in ans:
    i = int(i)
    cnt[i] += 1
for d in cnt:
    print(d)
