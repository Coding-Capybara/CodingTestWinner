def solution(citations):
    
    citations = sorted(citations)
    papers = len(citations)
    
    for i in range(papers):
        if citations[i] >= papers - i:
            return papers - i
    
    return 0
