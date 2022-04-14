import sys
a = int(input())
for _ in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print(b + c)

# 이 문제의 요점은 입력값을 input 이 아니라 sys.stdin.readline()으로 읽어올 수 있는 가가 요점이다