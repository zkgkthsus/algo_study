x, y, w, h = map(int, input().split())
c, d = w - x, h - y
print(min(x, y, c, d))
