n, m = map(int,input().split())
lec = list(map(int,input().split()))

left = max(lec)
right = sum(lec)

answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    bluray = 1

    for time in lect:
        if total + time > mid:
            bluray += 1
            total = 0
        total += time

    if bluray <= m:
        answer = mid
        right = mid - 1
    else:
        start = mid + 1

print(answer)
    
