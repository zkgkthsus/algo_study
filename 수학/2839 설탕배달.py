a = int(input())
ans = -1

cnt = a // 5
while cnt != -1:
    b = a -(cnt * 5)
    if b == 0:
        ans = cnt
        break
    if b % 3 == 0:
        ans = cnt + (b // 3)
        break
    cnt -= 1
print(ans)
