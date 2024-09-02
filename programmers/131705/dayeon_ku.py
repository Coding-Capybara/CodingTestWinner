from itertools import combinations

def solution(number):
    temp = list(map(lambda x: sum(x) == 0, combinations(number, 3)))
    count = temp.count(True)
    
    return count