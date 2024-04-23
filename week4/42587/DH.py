from collections import deque
def solution(priorities, location):
    answer = 0
    ls = []
    q = deque()
    for i,j in enumerate(priorities):
        q.append((i,j))
    while q:
        a = q.popleft()
        if q and any(a[1] < b[1] for b in q):
            q.append(a)
        else:
            ls.append(a)
    for i in ls:
        if i[0] == location:
            answer = ls.index(i)+1
    return answer