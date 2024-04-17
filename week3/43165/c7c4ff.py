answer = 0

def dfs(i, cnt, numbers, target):
    global answer
  
    if i == len(numbers):
        if cnt == target:
            answer += 1
        return
      
    dfs(i+1, cnt+numbers[i], numbers, target)
    dfs(i+1, cnt-numbers[i], numbers, target)
    return
    
    
def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    
    return answer
