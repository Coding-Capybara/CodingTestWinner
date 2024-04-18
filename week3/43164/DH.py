answer = []
def dfs(idx, count, visited, tickets,temp):
    if count == len(tickets):
        answer.append(temp)
        return
    for i in range(len(tickets)):
        # 이전 도착지와 출발지가 동일하고 방문한 적이 없는 경우
        if tickets[i][0] == tickets[idx][1] and visited[i]==0:
            visited[i] = 1
            dfs(i, count+1,visited, tickets, temp + [tickets[i][1]])
            visited[i] = 0


            
def solution(tickets):
    tickets = sorted(tickets, key = lambda x:(x[0],x[1]))
    start = 'ICN'
    for i in range(len(tickets)):
        visited = [0] * len(tickets)
        if tickets[i][0] == start:
            visited[i] = 1
            temp = ["ICN", tickets[i][1]]
            count = 1
            dfs(i, count, visited, tickets, temp)
    
    return answer[:][0]
