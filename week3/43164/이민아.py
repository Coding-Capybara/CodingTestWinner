from collections import defaultdict
def solution(tickets):
    answer = []
    #1.
    tickets.sort(key = lambda x : (x[0],x[1]))
    
    #2.
    loc_dict = defaultdict(list)
    for s, e in tickets:
        loc_dict[s].append(e)
    
    #3.
    route = ["ICN"]

    #4
    while route:
        loc = route[-1] #현재 위치 : route의 맨 마지막 원소
        #4-1.
        if loc not in loc_dict or len(loc_dict[loc]) == 0:
            answer.append(route.pop())
        #4-2.
        else:
            route.append(loc_dict[loc].pop(0))
    
    return answer[::-1]
