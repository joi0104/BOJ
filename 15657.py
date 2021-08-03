def select_x(index, selected):
    if len(selected) == m:
        print(*selected)
        return
    for i in range(index, n):
        select_x(i, selected + [x[i]])

n, m = map(int, input().split())
x = [str(i) for i in sorted(map(int, input().split()))]
select_x(0, [])
