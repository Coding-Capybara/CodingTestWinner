#스택으로 가능할듯?
#1. stack 리스트에 s[0] 넣기
#2. 다음 문자열이 s[-1]과 같다면 pop, 아니라면 append
#3. if not stack: 1, else: 0
def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
        
    if not stack:
        return 1
    else:
        return 0