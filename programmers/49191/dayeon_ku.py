# 위상 정렬 구현해봤다가 정렬만 해주고 경기에 대한 정보는 얻을 수 없었어서 폐기
# 플로이드 워셜
def solution(n, results):
    rank = [[0] * (n + 1) for _ in range(n + 1)]
    
    for a, b in results:
        rank[a][b] = 1 # a가 b한테 이김
        rank[b][a] = -1 # b가 a한테 짐
        
    for i in range(n + 1): # 경유
        for j in range(n + 1): # 시작
            for k in range(n + 1): # 끝
                if j == k:
                    continue
                
                # j가 i를 이기고 i가 k를 이김 -> j가 k를 이김
                if rank[j][i] == 1 and rank [i][k] == 1:
                    rank[j][k] = 1 # 이김
                    rank[k][j], rank[k][i], rank[i][j] = -1, -1, -1 # 짐
                    
    rankable = 0
    
    # 순위가 매겨지려면 n - 1번의 경기를 수행했어야 함
    # 0이 1개면 n - 1번의 경기를 했다는 의미 -> 정확한 순위를 알 수 있다
    # index와 선수의 숫자를 맞추기 위해 0번째 index는 사용하지 않았기 때문에 r.count(0) == 2 로 함
    for r in rank:
        if r.count(0) == 2:
            rankable += 1
    
    return rankable
    
                    