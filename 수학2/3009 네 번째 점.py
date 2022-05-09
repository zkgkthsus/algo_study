a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
x = [a[0], b[0], c[0]]
y = [a[1], b[1], c[1]]
ans = []
for i in x:
    if x.count(i) == 1:
        ans.append(i)
for j in y:
    if y.count(j) == 1:
        ans.append(j)
print(*ans)