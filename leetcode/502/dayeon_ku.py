# 시간초과 뜸..
# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         ans = w
        
#         while k > 0:
#             avail = [(p, idx) for idx, p in enumerate(profits) if capital[idx] <= w]

#             if not avail:
#                 break
#             else:
#                 p_val, index = max(avail)[0], max(avail)[1]
#                 ans += p_val
#                 w += p_val
#                 del capital[index], profits[index]
#                 k -= 1
        
#         return ans

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prj = [(capital[i], profits[i]) for i in range(len(profits))]
        prj.sort()
        max_heap = []
        i = 0

        for _ in range(k):
            while i < len(profits) and prj[i][0] <= w:
                heapq.heappush(max_heap, -prj[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)

        return w