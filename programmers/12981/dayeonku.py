# Lv.2 영어 끝말잇기
def solution(n, words):
    answer = []
    dummy = words.copy()
    
    prev = dummy[0]
    for i, w in enumerate(dummy):
        if i == 0:
            continue
            
        if w in words[:i] or w[0] != prev[-1]:
            person = (i+1) % n if (i+1) % n != 0 else n
            r = (i+1) // n + 1 if (i+1) % n != 0 else (i+1) // n
            answer.extend([person, r])
            break
        else:
            prev = w
    
    return answer if answer else [0, 0]