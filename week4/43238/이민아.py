def solution(n, times):
    answer = 0
    #1.
    times.sort()
    #2.
    start = times[0]
    #3.
    end = times[-1] * n
    while start <= end:
        #4.
        mid = (start+end)//2
        #5.
        screening_p = sum(list(map(lambda x : mid//x, times)))
        #6.
        if screening_p >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer