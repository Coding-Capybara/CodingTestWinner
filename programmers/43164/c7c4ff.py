from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for FROM, TO in sorted(tickets, key=lambda x: (x[0], x[1])):
        graph[FROM].append(TO)
        
    route = []
    
    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        route.append(start)
        
    dfs("ICN")
    
    return route[::-1]
