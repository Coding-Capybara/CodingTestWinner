# 효율성 테스트 미통과 ver.
def solution(stones, k):
    answer = 0
    while True:
        answer += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1
        cnt = 0
        for stone in stones:
            if stone == 0:
                cnt += 1
                if cnt == k:
                    return answer
            else:
                cnt = 0
    