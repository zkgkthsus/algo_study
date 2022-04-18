a_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', "PQRS", "TUV", "WXYZ"]
a = input()

ans = 0
for i in a:
    for c in a_list:
        if i in c:
            ans += a_list.index(c) + 3
            continue
print(ans)
# 초기 ord()를 사용해서 풀려고 했지만 "PQRS"와 "WXYZ" 가 있어서 노선 변경