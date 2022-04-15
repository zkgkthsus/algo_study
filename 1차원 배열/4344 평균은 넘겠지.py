a = int(input())
for _ in range(a):
    stu = list(map(int, input().split()))
    b = stu[0]
    score = 0
    cnt = 0
    for i in range(1, b+1):
        score += stu[i]
    avg = score / b
    for i in range(1, b+1):
        if stu[i] > avg:
            cnt += 1
    per = cnt / b * 100

    print(f'{per:0.3f}%')