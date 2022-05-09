while True:
    d = list(map(int, input().split()))
    d.sort()
    # print(d)
    a, b, c = d[0], d[1], d[2]
    if a == b == c == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")