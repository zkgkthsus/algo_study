cnt = []
other = 0

for _ in range(10):
    a = int(input())
    b = a % 42
    if b not in cnt:
        cnt.append(b)
print(len(cnt))