from collections import deque

def solution(progresses, speeds):
    answer = []
    days_required = deque()
    
    for i in range(len(progresses)):
        check = (100 - progresses[i]) / speeds[i]
        if check - int(check) != 0:
            days_required.append(int(check) + 1)
        else:
            days_required.append(int(check))
    
    release = 1
    first = days_required.popleft()
    while days_required:
        second = days_required.popleft()
        
        if first >= second:
            release += 1
        else:
            answer.append(release)
            release = 1
        
        first = max(first, second)
        
    answer.append(release)
            
    return answer