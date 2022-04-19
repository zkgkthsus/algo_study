a = int(input())
milab = 1
cnt = 1
while milab < a:
    milab += cnt * 6
    cnt += 1
print(cnt)

# 너무 어렵게 생각했다.
# 기존 밀랍수에 현재 차수 * 6만 더하기만 하면 되는데