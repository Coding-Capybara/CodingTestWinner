#1. 테스트 실패 -> 9,5,3,30,34 => 9533034. 정답인 9534330과 다름
# #1. numbers => str로 변경, 첫째자리 수 기준 내림차순 정렬
# #2. 문자 이어붙이기
# def solution(numbers):
#     answer = ''
#     numbers = sorted(map(str,numbers), key=lambda x:x[0], reverse=True)
#     for i in numbers:
#         answer += "".join(i)
#     print(answer)
#     return answer

#2. 성공
def solution(numbers):
    answer = ''
    #1,2
    numbers = sorted(map(str,numbers), key=lambda x:x*4, reverse=True)
    #3.
    for i in numbers:
        answer += "".join(i)
    #4.
    return str(int(answer))
