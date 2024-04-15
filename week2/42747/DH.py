def solution(citations):
    answer = 0
    ls = [0]
    for j in range(len(citations)):
        i = j+1
        cnt = 0
        for c in citations:
            if c >= i:
                cnt += 1
        if cnt >= i:
            ls.append(i)
    answer = max(ls)
    return answer