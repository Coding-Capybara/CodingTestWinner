def solution(triangle):
    answer = 0
    l = len(triangle)-1
    for i in range(l):
        for j in range(l-i):
            triangle[l-i-1][j] += max(triangle[l-i][j],triangle[l-i][j+1])
        answer = triangle[0][0]
    return answer