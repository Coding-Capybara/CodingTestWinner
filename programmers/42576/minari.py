#1. participant, completion정렬
#2. completion 길이만큼 반복, 만약 중간에 completion에 없는 이름이 있다면 => 정답
#3. 없다면 => participant 마지막 값이 정답
def solution(participant, completion):
    answer = ''
    #1.
    participant.sort()
    completion.sort()
    #2.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    #3.
    return participant[-1]