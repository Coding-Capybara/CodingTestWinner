from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    times = deque()
    trucks = deque(truck_weights)
    weights = 0
    time = 0
    stack = []
    while True:
        time += 1
        # 다리를 다 건넌 트럭은 뺴주기
        if bridge and time - times[0] == bridge_length:
            times.popleft()
            t = bridge.popleft()
            weights -= t
            stack.append(t)
            if len(stack) == len(truck_weights):
                return time
        # 다리에 트럭 추가 조건
        if trucks and weights + trucks[0] <= weight:
            t = trucks.popleft()
            weights += t
            bridge.append(t)
            times.append(time)