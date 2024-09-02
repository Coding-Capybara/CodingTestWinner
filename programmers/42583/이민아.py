from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0 # 걸린 초 세기
    bridge = deque([0] * bridge_length) #다리 길이만큼 리스트
    w = 0 #다리 위에 올라가있는 무게
    truck = deque(truck_weights) #남은 truck 리스트
    #1.
    while bridge:
        #2.
        cnt += 1
        w -= bridge[0]
        bridge.popleft()
        #3.
        if truck:
            if w + truck[0] <= weight:
                w += truck[0]
                bridge.append(truck.popleft())
            #3-1.
            else:
                bridge.append(0)
                
    return cnt