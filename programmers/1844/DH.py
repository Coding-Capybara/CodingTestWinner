from collections import deque

def solution(maps):
    answer = 0
    n=len(maps)
    m = len(maps[0])
    visited = [[0]*m for i in range(n)]
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visited[x][y] = 1
        while q:
            x,y = q.popleft()
            for i in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x+i[0], y+i[1]
                if not in_range(nx,ny):
                    continue
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

        return visited[n-1][m-1]

    answer = bfs(0,0)
    if answer == 0:
        return -1
    else:
        return answer