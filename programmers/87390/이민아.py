#1. 실패 : 시간초과, 2중for문 때문일 것으로 예상
#nxn 2차원 배열 생성
#n행까지라면
#1행 : 1~n
#2행 : 2,2~n
#3행 : 3,3,3~n..

#1. 각 행마다 돌면서 숫자 채우기
#1-1. 만약 i행의 i열 이하라면 i+1 채우기
#1-2. 만약 i행의 i열 초과라면 j+1채우기
#2. arr[left:right+1] 슬라이싱

def solution(n, left, right):
    arr = []
    #1.
    for i in range(n): #i = 행
        for j in range(n): #j = 열
            #1-1. 만약 i행의 i열 이하라면 i+1 채우기
            if j <= i:
                arr.append((i+1))
            #1-2. 만약 i행의 i열 초과라면 j+1채우기
            else:
                arr.append((j+1))
    #2
    return arr[left:right+1]


#2. 실패 : 시간초과. for문이 하나인데도..

#1. cnt로 현재 몇 번째 행인지 세기
#2. for문으로, cnt행까지 i+1, 이후부터는 인덱스+1 채우기
#3. 1의 2차원 리스트 => 1차원 리스트로 변경
#4. arr[left:right+1] 로 슬라이싱

def solution(n, left, right):
    arr = []
    #1.
    cnt = 1 #행
    #2.
    for i in range(n): #i = 열
        lst = []
        lst.append([cnt]*(i+1))
        lst.append(list(range(cnt+1,n+1)))
        #3.
        arr += sum(lst, []) 
        cnt += 1    
    #4.    
    return arr[left:right+1]

#3. 성공. 수학 규칙을 생각해보아요
#수학 규칙..생각생각생각..
#아이디어 : 나눗셈의 나머지 이용하기
#1. left부터 right+1까지 for문 돌기, i//n과 i%n 중 max값 + 1

def solution(n, left, right):
    answer = []
    #1.
    for i in range(left,right+1):
        answer.append(max(i//n, i%n)+1)
    return answer