a = int(input())


def hanoi(x, start, end):
    if x == 1:
        print(start, end)
        return
    hanoi(x - 1, start, 6 - start - end)
    print(start, end)
    hanoi(x - 1, 6 - start - end, end)


# 막대가 1개 일 경우 이동횟수는 1 = 2 ** 1 -1
# 막대가 2개 일 경우 이동횟수는 3 = 2 ** 2 -1
# 막대가 3개 일 경우 이동횟수는 7 = 2 ** 3 -1
# 막대가 4개 일 경우 이동횟수는 15 = 2 ** 4 -1
# 따라서 횟수에 대한 공식은 2**n -1이다
print(2 ** a - 1)
hanoi(a, 1, 3)


