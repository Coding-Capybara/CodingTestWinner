#조합 이용
#1. numbers에 나올 수 
from itertools import combinations
def solution(numbers):
    nCr = list(combinations(numbers, 2))
    answer = []
    for i in range(len(nCr)):
        answer.append(nCr[i][0] + nCr[i][1])
    
    return sorted(set(answer))