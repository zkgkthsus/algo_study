a = int(input())
b = [0] * (a + 1)
for i in range(1, a+1):
    if i == 1:
        b[1] = 1
    else:
        b[i] = b[i-1]+b[i-2]
print(b[a])