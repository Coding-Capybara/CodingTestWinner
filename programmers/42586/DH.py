from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i,j in zip(progresses, speeds):
        # 100-진행상황// 스피드 는 며칠이 걸릴지
        # 나머지 처리를 위해 j-1을 더해줌
        q.append((100-i+j-1)//j)
    while q:
        cnt = 1
        now = q.popleft()
        for p in q:
            if now >= p:
                cnt += 1
            else:
                break
        answer.append(cnt)
        for _ in range(cnt-1):
            q.popleft()
        
    return answer