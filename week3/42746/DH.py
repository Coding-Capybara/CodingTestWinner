# 1차 제출 -> [0,0,0,0] 인 경우 0000이 되어 실패
# def solution(numbers):
#     ls = list(map(str, numbers))
#     ls.sort(key = lambda x: x*3, reverse=True)
#     answer = ''.join(ls)
#     return answer

def solution(numbers):
    ls = list(map(str, numbers))
    ls.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(ls)
    return str(int(answer))