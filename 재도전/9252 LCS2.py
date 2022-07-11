import sys
input = sys.stdin.readline
a = [0] + list(input().strip())
b = [0] + list(input().strip())
len_a = len(a)
len_b = len(b)
dp = [[""] * len_b for i in range(len_a)]
# 전체 문자열을 체크하면서
for i in range(1, len_a):
    for j in range(1, len_b):
        # 첫번째 문자열과 동일하면 이전 좌표 문자열과 현재 문자열을 추가
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        # 아니면
        else:
            # 첫번째 문자열이 한차수 앞이고 두번째 좌표가 현재차수인 시점의 문자열이
            # 첫번째 문자열이 현재차수이고 두번째 좌표가 한차수 앞인 문자열보다 클때
            # 현재 좌표의 문자열을 갱신해준다.
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            # 아니면 계속해서 진행
            else:
                dp[i][j] = dp[i][j - 1]
print(len(dp[len_a - 1][len_b - 1]))
print(dp[len_a - 1][len_b - 1])