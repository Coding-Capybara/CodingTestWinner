def solution(storey):
    answer = 0
            
    while storey:
        flag = storey % 10
        if (flag == 5 and storey // 10 % 10 >= 5) or flag > 5:
            storey += 10 - flag
            answer += 10 - flag
        else:
            answer += flag
        storey //= 10
                
    return answer