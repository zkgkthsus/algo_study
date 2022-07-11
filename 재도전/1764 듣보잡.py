# 이문제의 요지는 리스트와 셋의 입력시간과 기능 특성을 이해해야하는 문제이다
# 그리고 알고리즘 문제 입력을 받을시 주의사항에 대한 공부도 될것이라 생각한다.
# 반복회수가 500000이상이 될수 있으므로 sys를 통해 입력을 받음
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
# 그리고 리스트를 입력받고 if문으로 확인하려고 할 때 시간초과 발생
# 따라서 set의 교집합 기능을 사용하려고 한다
a = set()
b = set()
for i in range(n):
    # 이때 스트립을 붙이는 이유는 strip을 붙이지 앞으면
    # abcd를 입력할때 abcd/n으로 입력된다.
    a.add(input().strip())
for j in range(m):
    b.add(input().strip())
# 그리고 set은 정렬이 되지 않으므로 리스트로 변환 후 정렬
c = sorted(list(a & b))

print(len(c))
for ans in c:
    print(ans)