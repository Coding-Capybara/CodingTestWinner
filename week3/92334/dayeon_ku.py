def solution(id_list, report, k):
    # 유저id : set(유저가 신고한 id)
    report_dict = {id:set() for id in id_list}
    # 신고 받은 횟수
    reported_count = {id:0 for id in id_list}
    
    # report split 해주기
    temp_list = list(map(lambda x: x.split(), report))
    for reporter, reportee in temp_list:
        # 같은 대상을 여러번 신고했는지 확인, 중복 신고는 1로 카운트
        if reportee not in report_dict[reporter]:
            reported_count[reportee] += 1
            
        report_dict[reporter].add(reportee)
    
    # k 보다 많이 신고 당한 사람만 filter
    k_check = list(filter(lambda x: x[1] >= k, reported_count.items()))
    answer_list = [0] * len(id_list)
    # k 보다 많이 신고 당한 사람이 report_dict의 value에 있으면 해당 key의 idx를 기준으로 answer_list 값 업데이트
    for reportee, _ in k_check:
        for idx, (k, v) in enumerate(report_dict.items()):
            if reportee in v:
                answer_list[idx] += 1
                
    return answer_list
        