a, b, c = map(int, input().split())
cnt = (c-a) // (a-b)
cnt2 = (c-a) % (a-b)
ans = 0
if cnt2 > 0:
    ans = cnt + 2
else:
    ans = cnt + 1
print(ans)