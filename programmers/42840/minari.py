#1. 각 학생의 맞은 갯수 저장할 lst 생성, 각 학생이 찍는 번호 학생 리스트에 저장
#2. 각 학생별 answers와 찍은 번호 대조, 맞은 갯수 cnt에 저장
#3. 가장 높은 점수 max_score에 저장, max_score와 점수가 같다면 ans에 인덱스+1로 저장
def solution(answers):
    #1.
    cnt = [0,0,0]
    stu1 = [1, 2, 3, 4, 5] #5
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5] #8
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10
    
    #2.
    #student1
    stu1 = stu1*2000
    for i in range(len(answers)):
        if stu1[i] == answers[i]:
            cnt[0] += 1
    
    #student2
    stu2 = stu2*2000
    for i in range(len(answers)):
        if stu2[i] == answers[i]:
            cnt[1] += 1
    
    #student3
    stu3 = stu3*2000
    for i in range(len(answers)):
        if stu3[i] == answers[i]:
            cnt[2] += 1
    
    #3.
    ans = []
    max_score = max(cnt)
    for i,score in enumerate(cnt):
        if score == max_score:
            ans.append(i+1)
    
    return ans