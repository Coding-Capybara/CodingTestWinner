def solution(k, m, score):
    length = len(score)
    
    score = sorted(score, reverse=True)
    sets = length // m
    total = 0
    
    for i in range(sets):
        if i == 0:
            total += score[:m][-1] * m
        else:
            total += score[i*m:i*m+m][-1] * m
        
    return total