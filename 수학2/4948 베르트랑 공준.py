
d = [True for _ in range(2*123456+1)]
d[0],d[1] = False,False

for i in range(2, int((123456 * 2+1)**0.5 +1)):
    if d[i]:
        j = 2
        while i*j <2*123456+1:
            d[i*j] = False
            j += 1
while True:
    a = int(input())
    cnt = 0
    if a == 0:
        break
    for i in range(a+1, 2*a+1):
        if d[i]:
            cnt += 1
    print(cnt)