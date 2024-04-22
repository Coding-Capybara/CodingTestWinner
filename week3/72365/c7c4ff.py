def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3)
    
    while numbers:
        answer += numbers[-1]
        numbers.pop()
        
    return str(int(answer))
