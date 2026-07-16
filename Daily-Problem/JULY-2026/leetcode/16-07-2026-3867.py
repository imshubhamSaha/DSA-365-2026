# 3867. Sum of GCD of Formed Pairs

class Solution:
    def gcd (self, a, b) :
        if a == 0 or b == 0 :
            return max(a,b) 
        if a > b :
            return self.gcd(a%b, b)
        return self.gcd(a, b % a)

    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        maxi = -1

        for i in range(n) :
            maxi = max(nums[i], maxi)
            prefix_gcd[i] = self.gcd(maxi, nums[i])

        prefix_gcd.sort()

        gcd_sum = 0

        left = 0
        right = n - 1

        while left < right :
            gcd_sum += self.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return gcd_sum

