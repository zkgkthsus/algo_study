croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
ans = 0
for c in croatia:
    while c in a:
        a = a.replace(c, " ",1)
        ans += 1
a = a.replace(" ", "")
print(len(a) + ans)
