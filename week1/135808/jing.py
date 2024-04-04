def solution(k, m, score):
    '''
    answer = 0
    # score 정렬
    score = sorted(score, reverse = True)
    
    # 사과를 m개씩 포장하고 최소값으로 점수 계산
    while (len(score) >= m):
        answer += score[m-1] * m
        score = score[m:]
    '''

    answer = 0

    # score를 정렬
    score = sorted(score, reverse = True)
    
    # m개를 기준으로 포장하며 점수 계산
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    
    return answer