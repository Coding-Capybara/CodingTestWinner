#1. 숫자 두 개 더하는 함수 생성
#2. 이중 for문으로 돌 수 있는 모든 경우의 수 반복해 더하기
#3. lst 중복 제거, 오름차순 정렬

def add(num1, num2):
    return num1 + num2


def solution(numbers):
    lst = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            lst.append(add(numbers[i],numbers[j]))
    lst = sorted(list(set(lst)))
    return lst