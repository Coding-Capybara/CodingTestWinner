def solution(a, b):
    answer = ''
    
    day = {3: 'SUN', 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI", 2: "SAT"}
    month = [31 , 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    date = (sum(month[:a-1]) + b) % 7
    answer = day[date]
    
    return answer