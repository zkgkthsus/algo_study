import sys
a = int(input())
for _ in range(1, a+1, 1):
    b, c = map(int, sys.stdin.readline().split())
    print(f'Case #{_}: {b + c}')