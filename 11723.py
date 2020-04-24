import sys
s = set()
for _ in range(int(sys.stdin.readline())):
    command, *num = sys.stdin.readline().split()
    if num: num = int(num[0])
    if command == 'add': s.add(num)
    elif command == 'remove':
        if num in s: s.remove(num)
    elif command == 'check':
        if num in s: print(1)
        else: print(0)
    elif command == 'toggle':
        if num in s: s.remove(num)
        else: s.add(num)
    elif command == 'all': s.update(range(1,21))
    elif command == 'empty': s.clear()

