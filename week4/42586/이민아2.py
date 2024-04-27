#1. progresses에 원소가 있을 때
#2. progresses 모든 리스트에 각 speeds를 더하기
#3. progresses[0]이 100이 넘을 때, pop & cnt += 1
#4. cnt가 0이 넘을 때 answer에 cnt 넣기
def solution(progresses, speeds):
    answer = []
    #1.
    while progresses:
        #2.
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        #3.
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        #4.
        if cnt > 0:
            answer.append(cnt)
    
    return answer