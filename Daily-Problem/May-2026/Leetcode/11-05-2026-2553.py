# 2553. Separate the Digits in an Array
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for num in nums :
            temp = num
            left = len(result) if len(result) > 0 else 0
            while temp :
                result.append((temp % 10))
                temp = temp // 10
            
            right = len(result) - 1

            while left < right :
                t = result[left]
                result[left] = result[right]
                result[right] = t
                left += 1
                right -= 1
        
        return result
