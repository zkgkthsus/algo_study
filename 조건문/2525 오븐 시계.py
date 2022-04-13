h, m = map(int, input().split())
cost = int(input())
if m + cost >= 60:
    m1 = (m + cost) % 60
    h += (m + cost) // 60
    if h >= 24:
        h = h % 24
else:
    m1 = m + cost
print(h , m1)