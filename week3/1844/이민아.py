from collections import deque
def solution(maps):
    #0.
    n = len(maps)
    m = len(maps[0])
    #1.상좌하우
    nr = [-1,0,1,0]
    nc = [0,-1,0,1]
    def bfs(r,c):
        queue = deque()
        queue.append((r,c))
        while queue:
            r,c = queue.popleft()
            for i in range(4):
                nnr = r + nr[i]
                nnc = c + nc[i]
                #3.
                #범위를 벗어나면 못가
                if nnr < 0 or nnr >= n or nnc < 0 or nnc >= m:
                    continue
                #벽이면 못가
                if maps[nnr][nnc] == 0:
                    continue
                #4.
                if maps[nnr][nnc] == 1:
                    queue.append((nnr,nnc))
                    #방문처리 + 갱신하기
                    maps[nnr][nnc] = maps[r][c] + 1
    #bfs 실행
    bfs(0,0)
    answer = maps[len(maps)-1][len(maps[0])-1]

    if answer == 1: #도달할 수 없는 경우
        answer = -1

    return answer          