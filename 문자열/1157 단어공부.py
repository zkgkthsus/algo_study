a = input().upper()
b = list(set(a))
anslist = []
for i in b:
    c = a.count(i)
    anslist.append(c)
if anslist.count(max(anslist)) > 1:
    print('?')
else:
    index = anslist.index(max(anslist))
    print(b[index])
# 이문제는 요주의