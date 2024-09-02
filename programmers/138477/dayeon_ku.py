def solution(k, score):
    ans = []
    topk = []
    
    for i in range(len(score)):
        topk = sorted(topk)
        if len(topk) < k:
            topk.append(score[i])
            ans.append(min(topk))
            continue
        elem = max(topk[0], score[i])
        topk[0] = elem
        ans.append(min(topk))
    
    return ans