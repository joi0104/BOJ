def grouping(n):
    tmp = []
    flag = False
    if len(n) == 5 : return ''.join(n)
    for operator in ['*','/','+','-']:
        for i in range(len(n)):
            tmp.append(n[i])
            if n[i] == operator:
                flag = True
                continue
            if flag:
                a, b, c = tmp.pop(), tmp.pop(), tmp.pop()
                tmp.append('('+c+b+a+')')
                flag = False
    return tmp

n = ['(']+list(input())+[')']
stack = []
answer = ''
for i in range(len(n)):
        stack.append(n[i])
        if n[i] == ')':
            tmp = stack.pop()
            tmp2 = [tmp]
            while tmp != '(':
                tmp = stack.pop()
                tmp2.append(tmp)
            stack += grouping(list(reversed(tmp2)))
    print(stack)
    n, stack = stack, []

n = ''.join(n)

for i in range(len(n)):
    stack.append(n[i])
    if n[i] == ')':
        stack.pop()
        right, root, left = stack.pop(), stack.pop(), stack.pop()
        stack.pop()
        stack.append(left+right+root)
print(stack[0])

