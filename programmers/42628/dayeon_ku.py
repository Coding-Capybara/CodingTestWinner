import heapq

def solution(operations):    
    h = []
    heapq.heapify(h)
    
    for oper in operations:
        o, num = oper.split()
        
        if o == "I":
            heapq.heappush(h, int(num))
        else:
            try:
                if num == "1":
                    h.pop()
                else:
                    heapq.heappop(h)
            except:
                pass
    
    if h:
        # heap의 마지막 값은 꼭 최대값이 아니기 때문에 sort를 해주던지, min() max() 함수를 사용해야 함
        return [max(h), min(h)]
    else:
        return [0, 0]
    