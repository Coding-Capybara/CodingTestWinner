def solution(citations):
    citations = sorted(citations, reverse=True)
    count = 0
    
    for i in range(len(citations)):
        if citations[i] <= count:
            break
            
        count += 1
            
    return count