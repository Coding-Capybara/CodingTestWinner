class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        s = 0
        hash_map = {0:1}

        for n in nums:
            s += n

            if s % k in hash_map:
                result += hash_map[s % k]
            # key가 hash_map에 존재하지 않으면 s % k : 0으로 넣어주기 (그리고 + 1)
            hash_map[s % k] = hash_map.get(s % k, 0) + 1

        return result