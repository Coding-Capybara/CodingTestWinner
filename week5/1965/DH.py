N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    temp = 1
    for j  in range(i):
        if arr[i] > arr[j]:
            if dp[j]+1 > temp:
                temp = dp[j] + 1
    dp[i] = temp
print(max(dp))