def solution(s):
    answer = True
    check = True
    cnt = 0
    leng = 0
    while check:
        for i in s:
            leng += 1
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            if cnt < 0 or leng == len(s):
                check = False
                break
                
    if cnt == 0:
        answer = True
    else:
        answer = False
        
    return answer
