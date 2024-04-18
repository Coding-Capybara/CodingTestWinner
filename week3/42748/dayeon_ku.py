def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        temp = array[i-1:j]
        answer.append(sorted(temp)[k-1])
        
    return answer