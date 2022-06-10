a = input()
b = len(a)
a = int(a)
c = a - (9 * b)
if c < 0:
    c = 0
while True:
    d = str(c)
    e = []
    for i in d:
        e.append(int(i))
    if a == c + sum(e):
        print(c)
        break
    c += 1
    if c == a:
        print(0)
        break
