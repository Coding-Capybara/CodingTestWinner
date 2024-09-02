import heapq

def solution(k, score):
    answer = []
    hof = []
    
    for i in range(len(score)):
        if k > len(hof):
            heapq.heappush(hof, score[i])
        else:
            if hof[0] < score[i]:
                heapq.heappop(hof)
                heapq.heappush(hof, score[i])
        
        answer.append(hof[0])
        
    return answer