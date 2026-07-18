# 1979. Find Greatest Common Divisor of Array
class Solution:
    def gcd(self, a, b) :
        if b == 0 :
            return a
        return self.gcd(b, a % b)


    def findGCD(self, nums: List[int]) -> int:
        n = len(nums)
        mx = nums[0]
        mn = nums[0]

        for num in nums :
            mx = max(mx, num)
            mn = min(mn, num)

        return self.gcd(mx, mn)
