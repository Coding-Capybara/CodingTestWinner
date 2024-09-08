#올바른 괄호면 true, 아니면 false
#1. 시작은 무조건 (여야함. )로 시작하면 false, cnt == 0일 때 )가 나와도 false
#2. (와 )의 개수 세기. (가 나오면 +1, )가 나오면 -1. 0이 되면 True, 아니면 False

def solution(s):
    cnt = 0
    for i in s:
        if cnt == 0 and i == ")":
            return False
        else:
            if i == "(":
                cnt += 1
            else:
                cnt -= 1
    
    if cnt == 0:
        return True
    else:
        return False
    

#스택
#1. (가 나오면 push, )가 나오면 pop
#2. isEmpty, pop이라면 false
#3. 탐색이 끝났을 때 isEmpty == True
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    else:
        return True