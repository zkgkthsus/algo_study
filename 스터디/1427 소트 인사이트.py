# 카운트정렬 사용
a = list(map(int,list(input())))
b = [0] * 10
for i in a:
    b[i] += 1
for j in range(len(b)-1, -1, -1):
    print(f'{j}' * b[j], end="")
