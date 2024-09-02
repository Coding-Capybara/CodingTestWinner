def solution(citations):
    cnt = 0 #h번 이상 인용된 논문의 횟수
    ans = 0 #h
    #1.
    min_n = min(max(citations), len(citations))
    #2.
    for i in range(min_n, 0, -1):
        for j in citations:
            if j >= i:
                cnt += 1
            else:
                pass
        #2-1.    
        if cnt >= i:
            ans = i
            break
        #2-2.
        else:
            cnt = 0
    #3.
    return ans