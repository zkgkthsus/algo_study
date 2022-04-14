a = int(input())
ans = -1
cnt = 0
while a != ans:
    cnt += 1
    if cnt == 1:
        b = a // 10
        c = a % 10
        if b+c < 10:
            ans = c * 10 + (b + c)
        else:
            ans = c * 10 + (b + c) % 10
    else:
        b = ans // 10
        c = ans % 10
        if b+c < 10:
            ans = c * 10 + (b + c)
        else:
            ans = c * 10 + (b + c) % 10
print(cnt)