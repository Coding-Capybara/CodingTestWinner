def solution(k, score):
    '''
    현재 명예의 전당에 오른 점수가 k개보다 적으면 명예의 전당에 추가
    if len(arr) < k:
        arr.append(i)
        answer.append(min(arr))
    # 그렇지 않으면 score를 확인해 명예의 전당에 추가
    else:
        if min(arr) <= i:
            arr.remove(min(arr))
            arr.append(i)
            answer.append(min(arr))
        else:
            answer.append(min(arr))
    ''' 
    # 명예의 전당 arr
    arr = []
    answer = []

    # score를 모두 확인
    for i in score:
        arr.append(i)
        
        if len(arr) > k:
            arr.remove(min(arr))
            
        answer.append(min(arr))

    return answer