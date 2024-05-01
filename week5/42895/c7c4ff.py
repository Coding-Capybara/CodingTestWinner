def solution(N, number):
    answer = -1
    
    dp = []
    
    for i in range(1, 9):
        cases = set()
        cases.add(int(str(N) * i))
    
        for j in range(0, i-1):
            for operator in dp[j]:
                for operator2 in dp[-j-1]:
                    cases.add(operator + operator2)
                    cases.add(operator - operator2)
                    cases.add(operator * operator2)
                    if operator2 != 0:
                        cases.add(operator // operator2)
                
                        
        dp.append(cases)
        
        if number in cases:
            answer = i
            break
        
    return answer


'''
dp[1]
2

dp[2]
22
2+2 2-2 2*2 2/2

dp[3]
222
2+(2+2) 2+(2-2) 2+(2*2) 2+(2/2)
2-(2+2) 2-(2-2) 2-(2*2) 2-(2/2)
2
'''
