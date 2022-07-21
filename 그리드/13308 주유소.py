import sys
input = sys.stdin.readline

# 문제의 핵심은
# 현재 주유소가 이전 주유소보다 기름이 싼지 확인 가능한가?
# 그럼 그 동안의 거리를 계산가능한가?
# 이다.


a = int(input())
di = list(map(int,input().split()))
cost = list(map(int,input().split()))

c = cost[0]
dist = 0
ans = di[0] * c
# 미리 계산한 이유는 반드시 사용되는 비용이기도 하며
# 반복문에서 제외하기 위해
for i in range(1, a -1):
    # 만약 기름값이 이전보다 적으면
    if cost[i] < c:
        ans += c * dist
        dist = di[i]
        c = cost[i]
    # 아니면 거리 추가
    else:
        dist += di[i]
    # 최종지점까지의 거리다 보니
    # 도착지점의 주유소의 가격은 고려할 필요 없다
    if i == a - 2:
        ans += c * dist
print(ans)


