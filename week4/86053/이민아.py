def solution(a, b, g, s, w, t):
    #1.
    start = min(t)
    lst = []
    for i in range(len(g)):
        lst.append((g[i]+s[i])//w[i]*t[i]*2)
    end = max(lst)
    answer = end
    #2.
    while start <= end:
        #채워진 gold, silver, time의 양
        gold = 0
        silver = 0
        deliver = 0
        mid = (start + end) // 2
        #3.
        for i in range(len(g)):
            #3-1.
            move = mid//(t[i]*2)
            if mid%(t[i]*2) >= t[i]: #한 번 더 옮길 수 있는지 없는지 판단
                move += 1
            gold += min(g[i], move * w[i])
            silver += min(s[i], move * w[i])
            deliver += min(g[i] + s[i], move * w[i])
        #4.
        if gold >= a and silver >= b and deliver >= a+b:
            answer = min(answer,mid)
            end = mid - 1
        #4-1.
        else:
            start = mid + 1
    return answer