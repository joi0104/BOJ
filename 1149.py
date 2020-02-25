N = int(input())
house = [list(map(int,input().split())) for i in range(N)]
dp = [[0]*3 for i in range(N+1)]
for i in range(N):
    dp[i + 1][0] = house[i][0] + min(dp[i][1], dp[i][2])
    dp[i + 1][1] = house[i][1] + min(dp[i][0], dp[i][2])
    dp[i + 1][2] = house[i][2] + min(dp[i][0], dp[i][1])
print(min(dp[N]))

'''
전에 발생한 상황을 고려해야 할때, dp를 사용한다.
내가 틀린부분은 R,G,B 상황 각각의 비용을 계산하지 않고 R,G,B 중 하나의 상황을 선택해서 계산하였다.
왜 이런 접근법이 문제인가? 만약 비용이 같은 경우가 여러번 나온다면 이에 대한 고려는 점점 뒤쪽으로 미뤄진다.
즉 앞의 많은 경우를 고려해야하는 경우가 생기기 떄문에 바로 하나 앞의 상황을 고려해서 선택하는 접근법은 틀렸다.
'''