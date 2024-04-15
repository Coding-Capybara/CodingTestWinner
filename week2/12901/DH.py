def solution(a, b):
    answer = ''
    ls = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU","FRI","SAT","SUN","MON","TUE", "WED"]
    count = 0
    for i in range(1,a):
        count += ls[i-1]
    print(count)
    count += b
    count %= 7
    answer = day[count]
    return answer