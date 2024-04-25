from collections import deque
def solution(prices):
    answer = []
    stock = deque(prices) 
    #1.
    while stock:
        #2.
        temp = 0 #현재 주식가격 저장할 변수
        cnt = 0 #주식가격이 언제 떨어졌는지 저장할 변수
        temp += stock.popleft()
        #3.
        for i in stock:
            if i >= temp:
                cnt += 1
            #3-1.
            else:
                cnt += 1
                break
        #4.
        answer.append(cnt)
    return answer