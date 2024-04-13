def solution(a, b):
    total_days = b
    day_dict = {3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU', 1:'FRI', 2:'SAT'}
    
    for month in range(1, a):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            total_days += 31
        elif month in [4, 6, 9, 11]:
            total_days += 30
        else:
            total_days += 29
    
    return day_dict[total_days % 7]