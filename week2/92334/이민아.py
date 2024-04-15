import collections
def solution(id_list, report, k):
    answer = []
    #1.
    report = set(report)
    #2.
    report_per = collections.defaultdict(list)
    #3.
    reported = collections.defaultdict(int)
    #4.
    for people in report:
        port, ported = people.split()
        #4-1.
        report_per[port].append(ported)
        #4-2.
        reported[ported] += 1
    #5.
    for port in id_list:
        cnt = 0
        for ported in report_per[port]:
            if reported[ported] >= k:
                cnt += 1
        answer.append(cnt)            
    
    return answer