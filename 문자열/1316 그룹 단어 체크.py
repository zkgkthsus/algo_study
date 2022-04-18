a = int(input())
ans = 0
for _ in range(a):
    check = []
    b = input()
    che_str = b[0]
    check.append(che_str)
    for i in range(1, len(b)):
        if che_str == b[i]:
            continue
        else:
            if b[i] in check:
                break
            if b[i] not in check:
                check.append(b[i])
                che_str = b[i]
    else:
        ans += 1
print(ans)