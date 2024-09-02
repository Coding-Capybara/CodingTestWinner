import datetime 

def solution(a, b):
    day = datetime.date(2016, a, b)
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    return week[day.weekday()]

###

def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = sum(month[:a-1])+b
    
    return day[days%7-1]
