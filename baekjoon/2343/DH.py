n,m = map(int, input().split())
arr = list(map(int,input().split()))
start = max(arr)
end = sum(arr)
while start <= end:
    # mid 는 최대 들어갈 수 있는 아이들의 합이 되어야 한다.
    mid =  (start + end) // 2 
    count = 1
    temp = 0
    for i in range(n):
        if temp + arr[i] > mid:
            temp = 0
            count += 1
        temp += arr[i]
    if count <= m:
        answer = mid
        end = mid -1
    else:
        start = mid + 1
print(answer)