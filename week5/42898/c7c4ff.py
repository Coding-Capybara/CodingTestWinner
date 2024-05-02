def solution(m, n, puddles):
    # watered_map = [[1] * m] * n
    # 이렇게 쓰면 메모리 값을 동일하게 가져가게 됨... 리스트 컴프리헨션 쓰기
    watered_map = [[1] * m for _ in range(n)]
    
    if puddles:
        for x, y in puddles:
            x, y = x-1, y-1
            
            # 예외처리. 맨 윗줄, 맨 왼쪽에 물이 있을 경우 그 경로도 없애주기
            if x == 0:
                for i in range(y, len(watered_map)):
                    watered_map[i][x] = 0
                    
            if y == 0:
                for i in range(x, len(watered_map[0])):
                    watered_map[y][i] = 0
                    
            watered_map[y][x] = 0
            
    for i in range(m):
        for j in range(n):
            # 맨 왼쪽 줄, 맨 윗 줄이 아니고, i, j가 범위 안에 있을 경우
            if i < len(watered_map[0]) and j < len(watered_map) and i != 0 and j != 0:
                if watered_map[j][i] != 0:
                    watered_map[j][i] = watered_map[j-1][i] + watered_map[j][i-1]

                
    answer = watered_map[-1][-1] % 1000000007
    
    return answer
