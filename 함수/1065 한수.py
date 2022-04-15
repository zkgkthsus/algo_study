def hansu(i):
    cnt = 0
    for a in range(1, i+1):
        if a < 10:
            cnt += 1
        elif a >= 10:
            b = list(str(a))
            e = 10
            for d in range(0, len(b)-1):
                if e == 10:
                    e = int(b[d]) - int(b[d+1])
                else:
                    if e != int(b[d]) - int(b[d+1]):
                        break
            else:
                cnt += 1
    return cnt

a = int(input())
ans = hansu(a)
print(ans)
