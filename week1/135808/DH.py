def solution(k, m, score):
    answer = 0
    # 최대 사과 점수: k
    # 한 상자 최대 사과 수: m
    # 사과들의 점수목록: score
    # 1.높은 점수 순대로 sort
    s = sorted(score, reverse = True)
    # 2.box 개수 구하기
    num_boxes = len(s) // m
    # 3.box마다 마지막 인덱스에 최대 사과 수 곱하기
    for i in range(num_boxes):
        box_max = s[m+(m*i)-1] * m
        answer += box_max
    return answer