from collections import deque

def solution(bridge_length, weight, truck_weights):    
    time_taken = 0
    q = deque(truck_weights)
    
    on_bridge = deque([0]*bridge_length)
    curr_w = 0
    while q:
        time_taken += 1
        curr_w -= on_bridge.popleft()

        if curr_w + q[0] > weight:
            on_bridge.append(0)
        else:
            curr = q.popleft()
            curr_w += curr
            on_bridge.append(curr)
            
    time_taken += bridge_length
            
    return time_taken