n, m = map(int,input().split())
card = list(map(int,input().split()))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            hab = card[i] + card[j] + card[k]
            if hab <= m and ans < hab:
                ans = hab
print(ans)