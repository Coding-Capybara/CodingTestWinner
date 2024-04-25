from collections import deque

def solution(priorities, location):
    answer = 0
    temp = []
    q = deque(priorities)
    process_idx = deque([i for i in range(len(priorities))])
    
    while q:
        priority = q.popleft()
        idx = process_idx.popleft()
        
        if any(num > priority for num in q):
            q.append(priority)
            process_idx.append(idx)
        else:
            temp.append(idx)

    return temp.index(location)+1