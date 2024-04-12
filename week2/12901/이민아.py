def solution(a, b):
    #1.
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    #2.
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #3.
    day = sum(months[:a-1]) + b
    #4.
    return weeks[(day%7)-1]