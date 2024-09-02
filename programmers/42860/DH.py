def solution(name):
    answer = 0
    alpha = {'A':0,'B':1,'C':2,'D':3,'E':4,
             'F':5,'G':6,'H':7,'I':8,'J':9,
             'K':10,'L':11,'M':12,'N':13,'O':14,
             'P':15,'Q':16,'R':17,'S':18,'T':19,
             'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    toggle = 0
    target = []
    max_try = len(name)-1
    ls = [max_try]
    for _ in name:
        target.append(alpha[_])
            
    def up_down(idx):
        if target[idx] <= 13:
            count = target[idx]
            return count
        else:
            count = (26-target[idx])
            return count
    for i in range(len(target)):
        toggle += up_down(i)
    answer += toggle
    for i in range(len(name)):
        moved= i+1
        while moved < len(name) and target[moved] == 0:
            moved += 1 
        # 갔다가 앗챠챠 뒤돌기
        shuttle = i*2
        remainder = len(name) - moved
        lookforward = shuttle + remainder
        # 뒤부터 돌아버려
        lookbehind = 2 * remainder + i
        ls.append(lookforward)
        ls.append(lookbehind)
    answer += min(ls)
    return answer