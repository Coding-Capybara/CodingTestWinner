from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer

# def solution(prices):
#     time = []
#     chk = []
    
#     for i in range(len(prices)):
#         time.append(0)
#         for j in range(len(prices[:i])):
#             if j in chk:
#                 pass
#             else:
#                 time[j] += 1
#                 if prices[i] < prices[j]:
#                     chk.append(j)
                
#     return time
