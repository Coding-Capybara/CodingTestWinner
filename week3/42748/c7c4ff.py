def solution(array, commands):
    answer = []
    
    for cnt in range(len(commands)):
        i = commands[cnt][0] - 1
        j = commands[cnt][1]
        k = commands[cnt][2] - 1
        
        arr = array[i:j]
        arr.sort()

        answer.append(arr[k])
        
            
    return answer
