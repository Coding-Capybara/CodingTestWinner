from collections import deque
def solution(s):
    answer = True
    q = deque()
    for i in s:
        q.append(i)
    a = q.popleft()
    cnt = 1
    if a == '(':
        while q:
            next_a = q.popleft()
            if next_a == ')':
                cnt -= 1
                if cnt < 0:
                    break
            else:
                cnt += 1
        if cnt != 0:
            return False
        else: 
            return True
    else:
        return False