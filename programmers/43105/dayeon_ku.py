# bottom-up으로 삼각형 가장 밑에서부터 더 큰 수를 더하면서 올라오기
def solution(triangle):        
    for i in range(len(triangle)-1, 0, -1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
        
    return triangle[0][0]