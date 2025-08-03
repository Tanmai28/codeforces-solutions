t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    dp = [-1] * (n + 2)  
    dp[n] = 0
    dp[n + 1] = 0
 
    for i in range(n - 1, -1, -1):
        if s[i] == '*':
            dp[i] = -1
            continue
 
        max_next = -1
        if i + 1 < n and s[i + 1] != '*':
            max_next = max(max_next, dp[i + 1])
        if i + 2 < n and s[i + 2] != '*':
            max_next = max(max_next, dp[i + 2])
        if max_next == -1:
            max_next = 0  
 
        dp[i] = max_next + (1 if s[i] == '@' else 0)
 
    print(dp[0])
