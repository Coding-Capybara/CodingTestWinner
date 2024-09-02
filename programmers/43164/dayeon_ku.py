'''
알파벳 순서만 고려함. 모든 도시를 방문할 수 없는 경우는 주어지지 않는다는 제한사항에 부합하지 않음.
answer = []

def solution(tickets):
    global answer
    visited = [False]*len(tickets)
    tickets = sorted(tickets, key=lambda x: x[1])
    print(tickets)
    dfs(tickets, visited, "ICN", 0)
    
    return answer

def dfs(tickets, visited, depart, idx):
    global answer
    
    if len(answer) == len(tickets):
        answer.append(tickets[idx][1])
        return
    
    for i in range(len(tickets)):
        if tickets[i][0] == depart:
            if not visited[i]:
                visited[i] = True
                answer.append(depart)
                dfs(tickets, visited, tickets[i][1], i)
'''

answer = []

def solution(tickets):
    global answer
    visited = [False]*len(tickets)
    dfs(tickets, visited, ["ICN"])
    
    # 알파벳순으로 정렬후 가장 앞에 있는 리스트를 반환
    return sorted(answer)[0]


def dfs(tickets, visited, templist):
    global answer
    
    # 모든 티켓을 다 쓴 경로가 있다면 answer에 넣기
    if len(templist) == len(tickets)+1:
        answer.append(templist)
        return
    
    # 백트래킹
    for i in range(len(tickets)):
        if not visited[i] and tickets[i][0] == templist[-1]:
            visited[i] = True
            dfs(tickets, visited, templist+[tickets[i][1]])
            visited[i] = False
                