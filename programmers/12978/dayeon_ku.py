# 다익스트라 사용
import heapq

def solution(N, road, K):
    INF = int(1e9)
    
    start = 1
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    distance[start] = 0
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost)) # 양방향이기 때문에
    
    def dijkstra(start):
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for b, c in graph[now]:
                new_cost = dist + c

                if new_cost < distance[b]:
                    distance[b] = new_cost
                    heapq.heappush(q, (new_cost, b))
    
    
    dijkstra(start)

    return len(list(filter(lambda x: x <= K, distance)))