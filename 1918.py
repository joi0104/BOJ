def grouping(N):
    flag = False
    for operator in [['*', '/'], ['+', '-']]:
        tmp = []
        for n in N:
            tmp.append(n)
            if flag:
                a, b, c = tmp.pop(), tmp.pop(), tmp.pop()
                tmp.append('(' + c + b + a + ')')
                flag = False
            if n in operator:
                flag = True
        N = [tmp[1]] if len(tmp) == 3 else tmp
    return ''.join(N)

N = ['('] + list(input()) + [')']
stack = []

for n in N:
    stack.append(n)
    if n == ')':
        tmp = [stack.pop()]
        while tmp[-1] != '(':
            tmp.append(stack.pop())
        stack.append(grouping(list(reversed(tmp))))

N, stack = ''.join(stack), []

for n in N:
    stack.append(n)
    if n == ')':
        stack.pop()
        right, root, left = stack.pop(), stack.pop(), stack.pop()
        stack.pop()
        stack.append(left + right + root)
print(''.join(stack))


