def solution(id_list, report, k):    
    # 신고한 id dict {id: set}
    reporter = {id: set() for id in id_list}
    # 신고 당한 id 횟수 dict {id: 0}
    reported = {id: 0 for id in id_list}
    # 처리 메일을 받을 횟수 list answer
    answer = [0] * len(id_list)
        
    # report 나누고 각 dict update
    for i in report:
        temp_reporter, temp_reported = i.split(" ")
        # 같은 신고자가 여러 번 신고하지 않았는지 확인
        if temp_reported not in reporter[temp_reporter]:
            reporter[temp_reporter].add(temp_reported)
            reported[temp_reported] += 1
            
    # k번보다 많이 신고된 id 확인
    k_reported = []
    for i in reported.items():
        if i[1] >= k:
            k_reported.append(i[0])
                        
    # 해당 아이디를 신고 reporter에 해당하는 answer list를 update
    for i in k_reported:
        for j in enumerate(reporter.items()):
            if i in j[1][1]:
                answer[j[0]] += 1
                
    return answer