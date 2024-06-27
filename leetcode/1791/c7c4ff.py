class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0], edges[1]

        if first[0] in second:
            return first[0]
        else:
            return first[1]
