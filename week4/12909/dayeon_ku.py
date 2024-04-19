def solution(s):    
    if s[0] == ")" or s[-1] == "(":
        return False
    
    o, c = 0, 0
    for parenthesis in s:
        if o < c:
            return False
        
        if parenthesis == "(":
            o += 1
        else:
            c += 1
    
    if o != c:
        return False
    return True