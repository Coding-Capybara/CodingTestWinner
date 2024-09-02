from itertools import combinations
def solution(number):
    answer = 0
    #1
    lst = list(combinations(number, 3))
    #2
    for i in lst:
        if sum(i) == 0:
            answer += 1
    return answer