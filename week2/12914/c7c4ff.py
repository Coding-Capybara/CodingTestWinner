def fib(n):
    cur, nextc = 0, 1
    for _ in range(n):
        cur, nextc = nextc, cur+nextc
        print(cur, nextc)
    
    return cur
    
def solution(n):
    answer = fib(n+1) % 1234567
    
    return answer