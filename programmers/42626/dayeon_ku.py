import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 0:
            return answer

        f = heapq.heappop(scoville)
        
        try:
            if f < K:            
                s = heapq.heappop(scoville)
                mixed = f + (s * 2)

                heapq.heappush(scoville, mixed)
                answer += 1
        except:
            return -1
        
    return answer