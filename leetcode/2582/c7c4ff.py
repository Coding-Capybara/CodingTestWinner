class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)
        pos = time % cycle

        if pos < n:
            return pos + 1
        else:
            return n - (pos - (n - 1))
