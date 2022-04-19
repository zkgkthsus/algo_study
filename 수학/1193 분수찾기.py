a = int(input())
ans = 0
cnt = 0
check = False
while True:
    cnt += 1
    if (ans + cnt) < a:
        ans += cnt
        check = not check
    else:
        break
if check:
    print(f'{a - ans}/{cnt -(a - ans)+1}')
else:
    print(f'{cnt -(a - ans)+1}/{a - ans}')