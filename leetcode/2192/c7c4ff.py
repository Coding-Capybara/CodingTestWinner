class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        output = [set() for _ in range(n)]
        indegree = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                output[neighbor].add(node)
                output[neighbor].update(output[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [sorted(list(ancestors)) for ancestors in output]

'''
시간초과..

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        output = [[] for _ in range(n)]

        for edge in edges:
            output[edge[1]].append(edge[0])

        for i in range(len(output)):
            for n in output[i]:
                output[i] += output[n]
        
            if output[i]:
                output[i] = list(set(output[i]))
                output[i].sort()

        return output
'''
