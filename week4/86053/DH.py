def solution(a, b, g, s, w, t):
    # a,b 는 타겟 금, 은
    # g, s 는 도시별 금,은 보유량
    # t는 편도시간, w는 최대 광물 이동가능량
    answer = -1
    start = 1
    end = max(t) * (a + b) * 2
    # mid 는 걸리는 총 소요 시간을 목표로
    # 주요 핵심은 해당 시간 내에 주어진 목표가 달성가능한지 여부

    while start <= end:
        gold, silver, total = 0, 0, 0
        mid = (start + end) // 2
        for i in range(len(g)):
            # 각 도시 별 한 번에 움직일 수 있는 금과 은 총량
            #해당 시간 내에 움직일 수 있는 횟수
            count = mid // (t[i] * 2)
            if mid % (t[i] *2) >= t[i]:
                count += 1
            # 실제 반복 가능한 횟수 * 운반 가능한 무게가 도시의 금보다 적을 경우
            if g[i] >= w[i] * count:
                gold += w[i] * count
            # 실제 반복 가능한 횟수 * 운반 가능한 무게가 도시의 금보다 많 경우
            # 있는 금 만큼만 더해주기
            else:
                gold += g[i]

            if s[i] >= w[i] * count:
                silver += w[i] * count
            else:
                silver += s[i]
            if g[i] + s[i] >= w[i] * count:
                total += w[i] * count
            else:
                total += g[i] + s[i]
        if gold >= a and silver >= b and total >= a + b:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
    return answer