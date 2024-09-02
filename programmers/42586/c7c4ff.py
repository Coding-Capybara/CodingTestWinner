import copy

def solution(progresses, speeds):
    answer = []
    date = []
    
    for i in range(len(progresses)):
        func = progresses[i]
        day = 0
        while func < 100:
            func += speeds[i]
            day += 1
        date.append(day)
    
    print(date)
    cnt = 1
    while date:
        s = date[0]
        if len(date) == 1:
            answer.append(cnt)
            break
        else:
            if s < date[1]:
                answer.append(cnt)
                date.pop(0)
                cnt = 1
            else:
                cnt += 1
                date.pop(1)

    return answer
