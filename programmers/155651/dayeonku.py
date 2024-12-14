# Lv.2 호텔 대실
# 패스가 안돼서 전에 풀었던 방법을 찾아봤음

import heapq

def solution(book_time):    
    time = []
    for s, e in book_time:
        hs, ms = map(int, s.split(":"))
        he, me = map(int, e.split(":"))
        time.append((hs * 60 + ms, he * 60 + me))
    
    heapq.heapify(time)
    print(time)
    
    answer = 0
    checkout = []
    
    while time:
        s, e = heapq.heappop(time)
        print(s, e)
        print(checkout)
        
        if not checkout:
            answer += 1
            checkout.append(e)
        else:
            for i, o in enumerate(checkout):
                if s >= o + 10:
                    print("?")
                    checkout[i] = e
                else:
                    answer += 1
                    checkout.append(e)
                break
    
    return answer

# 전에 풀었던 버전
# 로직은 같았지만 ... ㅎ.ㅎ
# from datetime import datetime, timedelta
# import heapq

# def solution(book_time):
#     time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
#     time.sort()
#     answer = 1
    
#     h = []
#     for s, e in time:
#         timechange = e + 10
        
#         if not h:
#             heapq.heappush(h, timechange)
#             continue
            
#         if s >= h[0]:
#             heapq.heappop(h)
#         else:
#             answer += 1

#         heapq.heappush(h, timechange)

#     return answer