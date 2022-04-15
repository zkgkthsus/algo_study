maxnum = -1000000
minnum = 1000000

a = int(input())
nlist = list(map(int, input().split()))
for i in range(a):
    if nlist[i] > maxnum:
        maxnum = nlist[i]
    if nlist[i] < minnum:
        minnum = nlist[i]
print(minnum, maxnum)
