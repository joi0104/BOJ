def check_sosu(end):
    for i in range(2, end+1):
        if is_sosu[i]:
            try:
                for j in range(2, end+1):
                    is_sosu[i*j] = False
            except:
                continue


start, end = map(int, input().split())
is_sosu = [True for _ in range(end+1)]
is_sosu[0], is_sosu[1] = False, False
check_sosu(end)

for i in range(start, end+1):
    if is_sosu[i]: print(i)