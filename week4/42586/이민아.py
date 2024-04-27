def solution(progresses, speeds):
    #2.
    answer = [[0,0]]
    for progress, speed in zip(progresses, speeds):
        #1.
        left = -((progress-100)//speed)
        #3,3-1
        if answer[-1][0] >= left:
            answer[-1][1] += 1
        else:
            answer.append([left,1])
    #4.
    answer = answer[1:]
    #5.
    return [i[1] for i in answer]