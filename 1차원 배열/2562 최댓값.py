maxnum = 0
index = 0

for i in range(1,10,1):
    a = int(input())
    if a > maxnum:
        maxnum = a
        index = i

print(maxnum)
print(index)