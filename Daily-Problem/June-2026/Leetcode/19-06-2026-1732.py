# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        pre_sum = 0
        max_gain = 0

        for i in range(n) :
            pre_sum += gain[i]
            max_gain = max(max_gain, pre_sum)

        return max_gain
