## 시간초과

# def solution(n, left, right):
#     answer = []
#     for i in range(1, n+1):
#         answer.extend([i] * i)
#         temp = [i for i in range(i+1, n+1)]
#         answer.extend(temp)

#     return answer[left:right+1]

##

def solution(n, left, right):
    answer = []
    
    for index in range(left, right + 1):
        row = index // n
        col = index % n
        
        answer.append(max(row, col) + 1)

    return answer

