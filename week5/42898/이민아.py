def solution(m, n, puddles):
    #1.
    maps = [[0 for i in range(m+1)] for j in range(n+1)]
    for y,x in puddles:
        maps[x][y] = -1
    #2.
    maps[1][1] = 1
    
    #3. 
    for r in range(1, n+1):
        for c in range(1, m+1):
            if maps[r][c] == -1:
                maps[r][c] = 0
                continue
            else:
                maps[r][c] += (maps[r-1][c] + maps[r][c-1]) % 1000000007
    return maps[n][m]