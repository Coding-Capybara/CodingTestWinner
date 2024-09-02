def solution(k, score):
    answer = []
    # 매 번 sort를 해줘야 하는가...
    # if 로 sort 횟수를 적게 해주느게 좋겠지?
    # score 횟수마다 반복
    ls = []
    for i in range(len(score)):
        # 1.리스트 내 값이 k개보다 적을 경우 추가(초반)
        if i < k:
            ls.append(score[i])
            ls = sorted(ls, reverse = True)
            answer.append(ls[-1])
        # 2. 리스트 내 최저값이 새로운 값보다 작을 경우
        elif ls[-1] < score[i]:
            del ls[-1]
            ls.append(score[i])
            ls = sorted(ls, reverse = True)
            answer.append(ls[-1])
        # 3. 리스트 내 최저값이 새로운 값보다 큰 경우
        else:
            answer.append(ls[-1])

    return answer