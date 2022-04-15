a = int(input())
score = list(map(int, input().split()))
maxsco = max(score)
sumsco = 0
for i in range(a):
    sumsco += score[i] / maxsco * 100
ans = sumsco / a
print(ans)