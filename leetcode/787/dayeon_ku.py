# 두번째 테케 안되는 코드
# import heapq

# class Solution:
#     def dijkstra(self, start, destination, graph, distance, k):
#         q = []
#         stop_count = 0

#         heapq.heappush(q, (0, start))
#         distance[start] = 0

#         while q:
#             dist, now = heapq.heappop(q)

#             if distance[now] < dist:
#                 continue

#             for node, c in graph[now]:
#                 cost = dist + c

#                 if cost < distance[node]:
#                     stop_count += 1
#                     if node == destination:
#                         if stop_count > k:
#                             distance[node] = cost
#                             return
#                     distance[node] = cost
#                     heapq.heappush(q, (cost, node))

#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         INF = int(1e9)

#         graph = [[] for _ in range(n + 1)]
#         distance = [INF] * (n + 1)

#         for a, b, c in flights:
#             graph[a].append((b, c))

#         self.dijkstra(src, dst, graph, distance, k)

#         print(distance)

#         if distance[dst] < INF:
#             return distance[dst]
#         else:
#             return -1

import heapq

class Solution:
    def dijkstra(self, start, destination, graph, distance, k):
        q = []
        visit = {}

        heapq.heappush(q, (0, start, 0))
        distance[start] = 0

        while q:
            dist, now, _k = heapq.heappop(q)

            if now == destination:
                return dist

            if now not in visit or visit[now] > _k:
                visit[now] = _k

                for node, c in graph[now]:
                    if _k <= k:
                        cost = dist + c
                        heapq.heappush(q, (cost, node, _k + 1))

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)

        graph = [[] for _ in range(n + 1)]
        distance = [INF] * (n + 1)

        for a, b, c in flights:
            graph[a].append((b, c))

        result = self.dijkstra(src, dst, graph, distance, k)

        if result:
            return result
        else:
            return -1