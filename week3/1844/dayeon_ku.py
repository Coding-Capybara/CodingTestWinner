from collections import deque

def solution(maps):
    return bfs(maps, 0, 0)


def bfs(maps, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
        
    if maps[-1][-1] <= 1:
        return -1
    else:
        return maps[-1][-1]