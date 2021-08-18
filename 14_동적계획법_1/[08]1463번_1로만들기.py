#1463번: 1로 만들기
#https://www.acmicpc.net/problem/1463


num = int(input())

dp = [0 for _ in range(num+1)]

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    
print(dp[num])
    
