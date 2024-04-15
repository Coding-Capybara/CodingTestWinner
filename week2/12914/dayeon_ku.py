def solution(n):
    # n으로 놓으면 타임아웃 뜸
    d = [0] * (n+1)
    d[0] = 1
    d[1] = 2
    
    # 피보피보..피보나치..
    for i in range(2, n):
        d[i] = d[i-1] + d[i-2]
        
    return d[n-1] % 1234567