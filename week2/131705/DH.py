def solution(number):
    answer = 0
    a=len(number)
    for i in range(a):
        for j in range(i+1,a):
            for k in range(j+1,a):
                if number[i]+number[j]+number[k] ==0:
                    print(i,j,k)
                    answer+=1
    return answer