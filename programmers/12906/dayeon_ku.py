from collections import deque

def solution(arr):
    q = deque(arr)
    answer = [q.popleft()]
    
    while q:
        curr = q.popleft()
        
        if answer[-1] != curr:
            answer.append(curr)

    return answer