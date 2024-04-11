import itertools

def solution(number):
    answer = 0
    
    total = list(itertools.combinations(number, 3))
    for combo in total:
        if sum(combo) == 0:
            answer += 1
            
    return answer
