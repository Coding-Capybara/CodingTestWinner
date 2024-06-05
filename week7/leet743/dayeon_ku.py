# sends the signal simulataneously
import heapq

class Solution:
    def dijkstra(self, start, distance, graph):
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        m = len(times)

        graph = [[] for i in range(n + 1)]
        distance = [INF] * (n + 1)

        for u, v, w in times:
            graph[u].append((v, w))

        self.dijkstra(k, distance, graph)

        result = distance[1:]

        if sum(d == INF for d in result) > 0:
            return -1
        else:
            return max(result)