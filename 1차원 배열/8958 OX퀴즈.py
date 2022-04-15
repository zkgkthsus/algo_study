a = int(input())
for _ in range(a):
    cnt = 0
    score = 0
    ans = input()
    for q in ans:
        if q == 'O':
            cnt += 1
            score += cnt
        elif q == 'X':
            cnt = 0
    print(score)