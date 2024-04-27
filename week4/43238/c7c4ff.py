def solution(n, times):
    answer = 0
    
    left, right = 1, times[-1] * n
    
    while left <= right:
        temp = 0
        mid = (left + right) // 2
        
        for time in times:
            temp += mid // time
            
        if temp >= n:
            answer = mid
            right = mid - 1
        elif temp < n:
            left = mid + 1
            

    return answer
