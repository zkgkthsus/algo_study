a = int(input())
c = [1 for i in range(10001)]
c[0], c[1] = 0, 0
for i in range(2, int(10000 ** 0.5) + 1):
    j = 2
    while i * j <= 10000:
        c[i * j] = 0
        j += 1
for _ in range(a):
    b = int(input())
    d = b // 2
    for k in range(d,1,-1):
        if c[b - k] == 1 and c[k] == 1:
            print(k, b - k)
            break
# 큰 차이가 없는 수를 찾기위해 목표수의 절반 지점에서 시작하고
# 현재 위치의 소수를 뺐을 때 뺀 값도 소수이면 정답
# 처음 풀이에서는 소수 전체를 체크해서 하려고 했지만 결과는 시간초과

