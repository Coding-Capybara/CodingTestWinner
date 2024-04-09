#1. 실패 : 시간 초과
#1. 2의 최대 개수 : n//2
#2. 2의 개수 + 나머지 1의 개수로 채운 list 여러개 생성..
#3. 각 리스트 별 조합 수 더하기..?
from itertools import permutations

def solution(n):
    answer = 0
    #1.
    two_n = n//2
    #2.
    lst = []
    for i in range(n//2+1):
        temp_lst = [2]*i
        temp_lst += [1]*(n-2*i)
        lst.append(temp_lst)
        temp_lst = []
    #3. 
    for comb in lst:
        comb_lst = list(set(map(tuple, permutations(comb, len(comb)))))
        answer += (len(comb_lst))       
    return answer%1234567

#2. 성공 : 피보나치 수열
#1,2,3,5,8,13,,,
#1. 0 + 1 < n=1일 때
#2. a, b = b, a+b 로 피보나치 수열 구현

def solution(n):
    #1.
    a, b = 0, 1
    #2.
    for i in range(n):
        a, b = b, a+b
        
    return b % 1234567