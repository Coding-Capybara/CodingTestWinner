[1번.] 실패(반례존재)
입력값 〉 3, [100, 30, 40, 150, 300, 200, 200]
기댓값 〉 [100, 30, 30, 40, 100, 150, 200]

def solution(k, score):
    #1.
    answer = [min(score[:k]) for i in range(k)]
    s_lst = score[:k]
    #2.
    for i in range(k,len(score)):
        #2-1.
        if score[i] >= min(s_lst):
            s_lst.remove(min(s_lst))
            s_lst.append(score[i])
        #2-2.
        answer.append(min(s_lst))

    return answer

[2번.]실패(런타임에러)

def solution(k, score):
    answer = []
    #1.
    honor = []
    for i in range(k):
        honor.append(score[i])
        answer.append(min(honor))
    #2.
    for j in range(k,len(score)):
        #2-1.
        if score[j] >= min(honor):
            honor.remove(min(honor))
            honor.append(score[j])
        #2-2.
        answer.append(min(honor))

    return answer

[3번.] 성공
!k > len(score)일 때 고려해야함!

def solution(k, score):
    answer = []
    #1.
    honor = []
    #2.
    if k <= len(score):
        for i in range(k):
            honor.append(score[i])
            answer.append(min(honor))
    #2-1.
    else:
        for i in range(len(score)):
            honor.append(score[i])
            answer.append(min(honor))
            
    #3.
    for j in range(k,len(score)):
        if score[j] >= min(honor):
            honor.remove(min(honor))
            honor.append(score[j])
        #4.
        answer.append(min(honor))
    return answer
