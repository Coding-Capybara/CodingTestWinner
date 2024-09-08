#함수 생성
def countans(stu, answers):
    cnt = 0
    stu = stu*2000
    
    for i in range(len(answers)):
        if stu[i] == answers[i]:
            cnt += 1
    return cnt

def solution(answers):
    cnt = [0,0,0]
    stu1 = [1, 2, 3, 4, 5] #5
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5] #8
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10

    cnt[0] = countans(stu1, answers)
    cnt[1] = countans(stu2, answers)
    cnt[2] = countans(stu3, answers)
    
    max_score = max(cnt)
    ans = []
    for i,score in enumerate(cnt):
        if score == max_score:
            ans.append(i+1)
    return ans