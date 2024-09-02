def score(n):
    if n == 1:
        return 3
    elif n == 2:
        return 2
    elif n == 3:
        return 1
    elif n == 4:
        return 0
    elif n == 5:
        return -1
    elif n == 6:
        return -2
    elif n == 7:
        return -3
    
def solution(survey, choices):
    answer = ''
    RTFCMJAN = [0, 0, 0, 0]
    
    for i in range(0, len(survey)):
        if survey[i] == "RT":
            RTFCMJAN[0] += score(choices[i])
        elif survey[i] == "TR":
            RTFCMJAN[0] -= score(choices[i])
        elif survey[i] == "CF":
            RTFCMJAN[1] += score(choices[i])
        elif survey[i] == "FC":
            RTFCMJAN[1] -= score(choices[i])
        elif survey[i] == "JM":
            RTFCMJAN[2] += score(choices[i])
        elif survey[i] == "MJ":
            RTFCMJAN[2] -= score(choices[i])
        elif survey[i] == "AN":
            RTFCMJAN[3] += score(choices[i])
        elif survey[i] == "NA":
            RTFCMJAN[3] -= score(choices[i])
    
    if RTFCMJAN[0] >= 0:
        answer += "R"
    else:
        answer += "T"
    if RTFCMJAN[1] >= 0:
        answer += "C"
    else:
        answer += "F"
    if RTFCMJAN[2] >= 0:
        answer += "J"
    else:
        answer += "M"
    if RTFCMJAN[3] >= 0:
        answer += "A"
    else:
        answer += "N"
        
    return answer
