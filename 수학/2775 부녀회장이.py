
a = int(input())
for _ in range(a):
    nu_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    fl = int(input())
    nu = int(input())
    for i in range(1,fl + 1):
        for j in range(1,nu):
            nu_list[j] += nu_list[j-1]
    print(nu_list[nu-1])
