def solution(k, m, score):
    #1.
    score.sort(reverse=False)
    #2.
    count = len(score)//m
    box = list()
    answer = 0
    #3.
    for i in range(count): 
        while len(box) < m: #box 안의 사과 개수가 m개가 될 때 까지만 반복
            box.append(score.pop())
        #3-1.
        answer += min(box) * m
        box = []
        
    return answer