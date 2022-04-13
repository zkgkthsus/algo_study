dice = list(map(int, input().split()))
cnt = 0
maxcnt = 0
number = 0
maxnum = max(dice)

for i in range(len(dice)):
    cnt = dice.count(dice[i])
    if cnt > maxcnt:
        maxcnt = cnt
        number = dice[i]

if maxcnt == 3:
    print(10000 + (number * 1000))
elif maxcnt == 2:
    print(1000 + (number * 100))
else:
    print(maxnum * 100)
