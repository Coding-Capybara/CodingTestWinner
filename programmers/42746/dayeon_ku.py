'''
시간초과 나옴
from itertools import permutations

def solution(numbers):
    answer = '0'
    for option in permutations(numbers, len(numbers)):
        temp = ''.join([str(num) for num in option])
        if int(temp) > int(answer):
            answer = temp
            
    return answer
'''
def solution(numbers):
    if all(num == 0 for num in numbers):
        return '0'
    
    strnum = [str(num) for num in numbers]
    sortednum = quick_sort(strnum)
    
    return ''.join(sortednum)
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left = []
    right = []
    for x in tail:
        templ = ''.join([x, pivot])
        tempr = ''.join([pivot, x])
        if templ > tempr:
            left.append(x)
        else:
            right.append(x)
            
    return quick_sort(left) + [pivot] + quick_sort(right)