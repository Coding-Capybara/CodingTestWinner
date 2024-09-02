def solution(n, left, right):
    leftx, rightx = left//n, right//n+1
    temp = [max(i+1, j+1) for i in range(leftx, rightx) for j in range(n)]

    return temp[left-(n*leftx):left-(n*leftx)+(right-left)+1]