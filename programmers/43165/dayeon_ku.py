answer = 0

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
        
    return answer

def dfs(numbers, target, idx, count):
    global answer
    
    if idx == len(numbers):
        if count == target:
            answer += 1
            return
        return
        
    dfs(numbers, target, idx+1, count+numbers[idx])
    dfs(numbers, target, idx+1, count-numbers[idx])