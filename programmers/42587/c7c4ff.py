def solution(p, l):

    answer = 0
    
    if len(p) == 1:
        answer = 1
    else:
        while p:
            first = p.pop(0)
            for i in range(len(p)):
                if first < p[i]:
                    check = False
                    p.append(first)
                    if l == 0:
                        l = len(p) - 1
                    else:
                        l -= 1
                    break
                else:
                    check = True
            if l == 0 and check:
                answer += 1
                break
            elif l != 0 and check:
                answer += 1
                l -= 1
                continue

    return answer
