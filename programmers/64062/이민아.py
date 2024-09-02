def solution(stones, k):
    answer = 0
    #1.
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            #2.
            if stone < mid:
                cnt += 1
            #2-1.
            else:
                cnt = 0
                
            if cnt >= k:
                break
        #3.
        if cnt >= k:
            end = mid - 1
        #3-1.
        else:
            answer = mid
            start = mid + 1
        
    return answer