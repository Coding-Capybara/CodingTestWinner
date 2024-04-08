def solution(k, m, score):
    max_profit = 0
    sorted_score = sorted(score, reverse=True)
    for i in range(m-1, len(sorted_score), m):
        max_profit += sorted_score[i]*m
        
    return max_profit