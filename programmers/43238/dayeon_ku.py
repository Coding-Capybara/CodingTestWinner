def solution(n, times):
    times.sort()
    min_time = 1
    max_time = max(times)*n
    return binary_search(times, n, min_time, max_time)

def binary_search(arr, target, start, end):
    while start <= end:
        people = 0
        mid = (start + end) // 2
        
        for t in arr:
            people += mid // t
            
            if people >= target:
                break
        
        if people >= target:
            end = mid - 1
        else:
            start = mid + 1
            
    return start