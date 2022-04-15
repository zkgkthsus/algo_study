a = int(input())
for _ in range(a):
    b, c = input().split()
    b = int(b)
    ans = ''
    for d in c:
        ans += d * b
    print(ans)