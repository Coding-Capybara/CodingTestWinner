from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
        is_course = []
        for o in orders:
            for option in combinations(o, n):
                temp = ''.join(sorted(option))
                is_course.append(temp)
                
        flag = 2
        for course, freq in Counter(is_course).most_common():
            if freq >= flag:
                flag = freq
                answer.append(course)
            else:
                break
    
    return sorted(answer)