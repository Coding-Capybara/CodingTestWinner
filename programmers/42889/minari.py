#실패율 : stage도달 && clearX / stage도달
#N : stage 개수
#stages : 사용자가 멈춰있는 stage 번호
#return : 실패율이 높은 stage부터 내림차순으로

#1. 해당 stage에 도달한 사용자 수 구하기
#2. 해당 stage에 남아있는 사용자 수 구하기
#3. 2/1 = 해당 stage의 실패율. fail에 저장
#4. fail의 큰 index+1부터 answer에 넣기

#실패 1,6,7,9,13,23,24,25 런타임에러
#원인 : succss가 0인 경우(스테이지에 도달한 사람이 없을 경우, 실패율 = 0)
def solution(N, stages):
    fail = [] #실패율 저장
    stages.sort()
    
    i = 1 #stage 번호
    while i <= N:
        success = sum(1 for x in stages if x>=i) #1. 성공한 사람의 수, #8,7,4,2,1 / 4,1,2,3
        fail.append((i, stages.count(i) / success)) #2,#3
        i += 1
    
    #4.
    fail.sort(key=lambda x : (-x[1], x[0]))
    return [stage for stage, _ in fail]

#성공
def solution(N, stages):
    fail = [] #실패율 저장
    stages.sort()
    
    i = 1 #stage 번호
    while i <= N:
        success = sum(1 for x in stages if x>=i) #1. 성공한 사람의 수, #8,7,4,2,1 / 4,1,2,3
        if success == 0:
            fail_rate = 0 #스테이지에 도달한 사람이 없을 경우 실패율 = 0
        else: 
            fail_rate = stages.count(i) / success
        fail.append((i, fail_rate))
        i += 1
    
    #4.
    fail.sort(key=lambda x : (-x[1], x[0]))
    return [stage for stage, _ in fail]
