#회전 횟수 = 문자열 수. n번 회전 시 만들어진 문자열에서 괄호가 올바른 지 확인, n+1번 회전 시 만들어진 문자열에서 괄호가 올바른 지 확인...
#1. 들어온 괄호가 여는괄호인지 확인, 맞다면 stack에 더하기
#1-1. 아니라면 잘못된 괄호, break
#2. 들어온 괄호가 닫는 괄호이고, stack의 마지막이 해당 여는 괄호일 때 stack.pop
#3. 전체가 다 돌았을 때 stack 리스트가 비어있다면 answer +1
def solution(s):
    answer = 0
    N = len(s)
    for i in range(N):
        stack = []
        for j in range(N):
            c = s[(i+j)%N]
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack: #stack 리스트가 비어있다면 = 짝이 맞지 않으면 break
                    break

            #stack에 쌓여있는 괄호들과 짝이 맞는지 확인
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()

        else:
            if not stack:
                answer += 1
            
    return answer