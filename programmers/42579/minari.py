#알아야할 것 : 장르 별 재생 횟수, 장르의 고유번호 & 재생 수 => 만약 재생 수가 같다면 고유번호가 낮은순부터 정렬되어야 함
#1. 장르별 총 재생횟수, 장르 고유번호 & 재생 수 담을 dict 생성
#2. genres와 plays를 돌면서 1의 dict에 담기
#3. 장르별 총 재생횟수, 장르 고유번호 & 재생수 담은 dict를 재생수 별로 내림차순 정렬
#4. 장르별 총 재생횟수 순서대로 앞 고유번호 두 개 answer에 더하기
from collections import defaultdict
def solution(genres, plays):
    answer = []
    #1.
    cnt_gr = defaultdict(int)
    grNpl = defaultdict(list)
    
    #2.
    j = 0
    for i in genres:
        cnt_gr[i] += plays[j]
        grNpl[i].append([j,plays[j]])
        j += 1
    
    #3.
    play_cnt = [] #장르를 재생수로 정렬하기 위한 리스트
    for i in cnt_gr:
        play_cnt.append([cnt_gr[i], i])
    play_cnt.sort(reverse=True)
    
    #4.
    for i in play_cnt:
        if len(grNpl[i[1]]) == 1: #장르의 개수가 1개뿐일때 i[1] : play_cnt의 pop, classic 부분
            answer.append(grNpl[i[1]][0][0])
        else:
            temp = grNpl[i[1]]
            temp.sort(key = lambda x: (-x[1],x[0])) #(-x[1],x[0]): 재생수 기준 내림차순, 고유번호순 오름차순 정렬
            answer.append(temp[0][0])
            answer.append(temp[1][0])
    return answer