a, b = map(int, input().split())
d = 2
for i in range(a, b+1):
    if i == 1:
        continue
    check = True
    for j in range(2,int(i ** 0.5)+1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
# 에라토스테네스의 체를 이용
