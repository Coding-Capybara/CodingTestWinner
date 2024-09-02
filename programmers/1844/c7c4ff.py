from collections import deque
            
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            # 상하좌우 4번
            for i in range(4):
                move_x = x + dx[i]
                move_y = y + dy[i]

                # 맵 밖으로 넘어가는 경우는 패스
                if 0 > move_x or 0 > move_y:
                    continue
                elif move_x >= len(maps) or move_y >= len(maps[0]):
                    continue

                # 0 : 벽인 경우 패스, 아직 가지 않은 1인 경우는 큐에 넣기
                # 움직인 경우 1씩 추가하는 것으로 갱신함
                if maps[move_x][move_y] == 0:
                    continue
                elif maps[move_x][move_y] == 1:
                    q.append((move_x, move_y))
                    maps[move_x][move_y] = maps[x][y] + 1
                
    bfs(0, 0)
    # 상대방 진영은 무조건 (n, m) 고정
    answer = maps[len(maps)-1][len(maps[0])-1]

    # 도달하지 못해 1이라면 -1 반환, 갱신됐다면 해당 숫자 반환
    if answer == 1:
        return -1
    else:
        return answer
