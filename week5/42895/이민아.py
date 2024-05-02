def solution(N, number):
    answer = 0
    #Memoization을 위한 리스트 초기화,최솟값이 8보다 크면 -1이므로
    lst = [set() for x in range(8)]
    for i, x in enumerate(lst, start=1):
        x.add(int(str(N)*i))
    #N을 i+1개 사용했을 때 만들 수 있는 숫자
    for i in range(len(lst)):
        for j in range(i):
            for num1 in lst[j]:
                for num2 in lst[i-j-1]:
                    lst[i].add(num1 + num2)
                    lst[i].add(num1 - num2)
                    lst[i].add(num1 * num2)
                    if num2 != 0:
                        lst[i].add(num1 // num2)
        
        if number in lst[i]: #N을 i+1번 사용했을 때 찾고자 하는 값 number가 존재하면 i+1 return
            answer = i+1
            break
        else:
            answer = -1
    
    return answer