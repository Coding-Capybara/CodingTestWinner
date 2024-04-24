def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    sumTruck = 0
    
    while truck_weights:
        answer += 1
        
        cur = bridge.pop(0)
        bridge.append(0)
        
        if cur != 0:
            sumTruck -= cur
        
        if sumTruck + truck_weights[0] <= weight:
            nextTruck = truck_weights.pop(0)
            sumTruck += nextTruck
            bridge[-1] = nextTruck
            
        if len(truck_weights) == 0:
            answer += bridge_length
    
            
    return answer
