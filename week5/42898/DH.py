def solution(m, n, puddles):
    answer = 0
    maps = [[0 for _ in range(m)] for __ in range(n)]
    maps[0][0] = 1
    for x in range(m):
        for y in range(n):
            if [x+1,y+1] not in puddles:
                if y <= n-2:
                    maps[y+1][x] += maps[y][x]
                if x <= m-2:
                    maps[y][x+1] += maps[y][x]
    
    return maps[-1][-1] % 1000000007