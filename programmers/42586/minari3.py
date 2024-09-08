#배포되어야하는 순서대로 작업의 진도 적어놓음
#1. progresses가 없을 때까지 진행.
#2. progresses의 각 원소에 speeds 원소를 더함. (1초)
#3. while progresses[0] >= 100: 만약 progresses[0]이 100보다 크거나 같다면, popleft(), cnt +=1
#3-1. 2,3번 반복
#4. 만약 progresses가 없다면 break
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    #1.
    while progresses:
        #2.
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        #3.
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            
        if cnt > 0:
            answer.append(cnt)
            
    return answer