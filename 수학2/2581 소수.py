a = int(input())
b = int(input())
d = []
for i in range(a, b+1):
    if i != 1:
        check = True
        # 범위를 현재 숫자까지로 한정 지으면서 자기자신에 대해서는 반복문이 작동을 하지 않는다
        # 예를 들어 i가 2 이면 범위가 range(2,2)이면 탐색할 범위가 없으므로 작동 x
        # i가 3일 경우 range(2,3)일경우 j는 2까지만 나오기 때문에 자기자신으로 나눌 경우가 없어
        # 반복문 안의 if 문을 피해간다.
        for j in range(2,i):
            if i % j == 0:
                check = False
                break
        if check:
            d.append(i)
if len(d) == 0:
    print("-1")
else:
    print(sum(d))
    print(d[0])
