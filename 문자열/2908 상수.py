a, b = input().split()
ra, rb = '', ''
for r in range(len(a)-1, -1, -1):
    ra += a[r]
for r in range(len(a)-1, -1, -1):
    rb += b[r]
if int(ra) > int(rb):
    print(ra)
else:
    print(rb)