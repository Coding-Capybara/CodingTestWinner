def solution(id_list, report, k):
    answer = [0] * len(id_list)
    archive = [[] for _ in range(len(id_list))]

    report_dict = {}
    
    for rep in report:
        temp = rep.split(" ")
        archive[id_list.index(temp[0])].append(temp[1])
    
    for i in range(len(archive)):
        archive[i] = set(archive[i])
        for result in archive[i]:
            try:
                report_dict[result] += 1
            except:
                report_dict[result] = 1
                
    final = list(filter(lambda v : v[1] >= k, report_dict.items()))
    
    for warned in final:
        for i in range(len(archive)):
            if warned[0] in archive[i]:
                answer[i] += 1
                
    return answer
