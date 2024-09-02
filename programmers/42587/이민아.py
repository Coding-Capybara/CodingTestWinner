def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    while True:
        temp = queue.pop(0)
        #2.
        if any(temp[1] < q[1] for q in queue):
            queue.append(temp)
        else:
            answer += 1
            #3.
            if temp[0] == location:
                return answer