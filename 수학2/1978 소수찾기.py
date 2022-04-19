n_list = [x for x in range(1001)]
for j in range(2,33):
    for i in range(len(n_list)-1,-1,-1):
        if n_list[i] == 0:
            continue

        if n_list[i] % j == 0 and n_list[i] // j != 1:
            n_list[i] = 0
n_list = sorted(list(set(n_list)))[2::]
a = int(input())
check = list(map(int,input().split()))
cnt = 0
for k in check:
    if k in n_list:
        cnt += 1
print(cnt)

# 에라토스테네스의 체를 이용하여 풀었다 해당범위내 소수를 골라내는데 탁월
