n, m = map(int,input().split())
lesson = list(map(int,input().split()))
#1.
start = max(lesson)
end = sum(lesson)
answer = end

while start <= end:
    mid = (start + end) // 2
    #2.
    cnt = 1
    pre_t = 0 
    for i in lesson:
        if pre_t + i > mid:
            cnt += 1
            pre_t = i
        else:
            pre_t += i
    #3.
    if cnt <= m:
        answer = mid
        end = mid - 1
    #4.
    else:
        start = mid + 1

print(answer)