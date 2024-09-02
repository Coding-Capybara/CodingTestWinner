def solution(n, times):
    start = 1
    end = max(times) * n
    answer = end
    while start <= end:
        people = 0
        mid = (start + end) // 2
        
        for time in times:
            people += (mid // time)
        
        if people < n :
            start = mid + 1
        
        else:
            answer = min(answer, mid)
            end = mid - 1    
    return answer