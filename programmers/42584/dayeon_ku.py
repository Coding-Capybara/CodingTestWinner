from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    time = 0
    while q:
        curr = q.popleft()
        
        for price in q:
            time += 1
            if price < curr:
                break
        answer.append(time)
        time = 0

    return answer