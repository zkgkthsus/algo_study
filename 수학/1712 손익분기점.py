a, b, c = map(int, input().split())
ans = -1
d = 0
if (c - b) > 0:
    ans = a // (c - b) + 1
    d = a % (c-b)
print(ans)
