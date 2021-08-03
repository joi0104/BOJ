def select_x(selected, length):
    if length == m:
        print(selected[1:])
        return
    for i in range(n):
        select_x(selected + x[i], length + 1)

n, m = map(int, input().split())
x = [' ' + str(i) for i in sorted(map(int, input().split()))]
select_x('', 0)

