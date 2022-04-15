self = [i for i in range(1,10001)]
# selflist = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]
def selfnum(i):
    a = list(str(i))
    point = 0
    for b in a:
        point += int(b)
    nextnum = point + i
    if nextnum <= 10000 and nextnum in self:
        self.remove(nextnum)
        selfnum(nextnum)
for i in range(1,10001):
    selfnum(i)
for d in self:
    print(d)
