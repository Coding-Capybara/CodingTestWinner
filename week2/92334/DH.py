def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {}
    re = {}
    a = list(set(report))
    # 각 id에 맞는 신고횟수 딕셔너리 생성
    # 신고자 딕셔너리 생성
    for i in id_list:
        id_dict[i] = 0
        re[i] = []
    # 딕셔너리에 신고횟수 저장
    for i in range(len(a)):
        x, y = a[i].split()
        id_dict[y] += 1
        re[y].append(x)
    # 중복 제거
    for i in id_list:
        re[i] = list(set(re[i]))
    for id in id_list:
        if id_dict[id] >= k:
            for i in range(len(re[id])):
                answer[id_list.index(re[id][i])] += 1
    
        
    return answer