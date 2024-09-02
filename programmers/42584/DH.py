from collections import deque
def solution(price):
    answer = []
    prices = deque(price)
    ccur = 1
    while prices:
        cur = prices.popleft()
        cnt = 0
        for i in range(ccur, len(price)):
            if cur <= price[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        ccur += 1
    return answer