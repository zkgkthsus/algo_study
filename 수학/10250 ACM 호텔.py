a = int(input())

for _ in range(a):
    H, W, N = map(int, input().split())
    ans = (N % H) * 100 + (N // H) + 1
    if (N % H) == 0:
        ans = (H) * 100 + (N // H)
    print(ans)

# (N % H)가 0일때를 고려 하지 못했다.