def solution(survey, choices):
    answer = ''
    
    # 각 지표를 dict로 정의
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # survey-choices에 따라 점수 계산
    for pair in zip(survey, choices):
        if pair[1] > 4:
            dic[pair[0][1]] += pair[1] % 4
        else:
            dic[pair[0][0]] += 4 - pair[1]
    
    # 계산한 점수에 따라 유형 구분
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer