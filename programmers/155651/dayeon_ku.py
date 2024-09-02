from datetime import datetime, timedelta
import heapq

def solution(book_time):
    # 총 시간 구하고 정렬하기
    time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    time.sort()
    answer = 1
    
    h = []
    for s, e in time:
        # 10분 청소시간 포함
        timechange = e + 10
        
        # heap에 아무 것도 없으면 넣기
        if not h:
            heapq.heappush(h, timechange)
            continue
        
        # 예약 받은 시간이 가장 이른 체크아웃 시간 보다 이르면 h에서 빼주기
        if s >= h[0]:
            heapq.heappop(h)
        # 아니라면 새로운 방 필요
        else:
            answer += 1

        heapq.heappush(h, timechange)

    return answer