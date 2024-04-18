def solution(array, commands):
    answer = []
    def knum(array, command):
        narr = array[command[0]-1:command[1]]
        narr.sort()
        numk = narr[command[2]-1]
        return numk
    for i in commands:
        numk = knum(array,i)
        answer.append(numk)
    return answer