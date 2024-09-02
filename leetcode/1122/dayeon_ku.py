class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {k:0 for k in arr2}
        extra = []

        for num in arr1:
            if num in arr2:
                hash_map[num] += 1
            else:
                extra.append(num)

        result = []
        for k, v in hash_map.items():
            result.extend([k] * v)
        
        result.extend(sorted(extra))

        return result