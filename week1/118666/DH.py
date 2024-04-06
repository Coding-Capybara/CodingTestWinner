def solution(survey, choices):
    answer = ''
    category = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
    for i in range(len(survey)):
        imsi = choices[i]-4
        if imsi < 0:
            category[survey[i][0]] += abs(imsi)
            print(category)
        elif imsi > 0:
            category[survey[i][1]] += imsi
    if category['R'] >= category['T']:
        answer += 'R'
    else: 
        answer += 'T'
    if category['C'] >= category['F']:
        answer += 'C'
    else: 
        answer += 'F'
    if category['J'] >= category['M']:
        answer += 'J'
    else: 
        answer += 'M'
    if category['A'] >= category['N']:
        answer += 'A'
    else: 
        answer += 'N'
    return answer