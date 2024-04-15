def solution(numbers, target):
    answer = 0
    def dfs(idx, number):
        if idx == len(numbers) and target == number:
            nonlocal answer 
            answer += 1
        elif idx == len(numbers):
            return
        else:
            dfs(idx+1, number + numbers[idx])
            dfs(idx+1, number - numbers[idx])
    dfs(0,0)     
    return answer