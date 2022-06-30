def solution(p):
    a = asdf(p)
    answer = ''
    if a:
        answer = p
    else:
        answer = Correct(p)

    return answer


def Correct(p):
    l = 0
    r = 0
    u = ''
    v = ''
    if len(p) == 0:
        return ''
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        elif p[i] == ')':
            r += 1
        if l != 0 and r != 0 and l == r:
            u = p[:l + r]
            v = p[l + r:]
            break
    if asdf(u):
        return u + Correct(v)
    else:
        return '(' + Correct(v) + ')' + qwer(u)


def asdf(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
    if stack:
        return False
    else:
        return True


def qwer(p):
    a = p[1:-1]
    b = ''
    for i in a:
        if i == '(':
            b = b + ')'
        else:
            b = b + '('
    return b