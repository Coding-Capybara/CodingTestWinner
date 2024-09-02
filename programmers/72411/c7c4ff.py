from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:
        new_menu = []
        for j in orders:
            com = combinations(j, i)

            for menu in com:
                temp = ''.join(sorted(menu))
                new_menu.append(temp)
        sorted_menu = Counter(new_menu).most_common()

        for k, v in sorted_menu:
            if v >= 2 and v == sorted_menu[0][1]:
                answer.append(k)

    return sorted(answer)
