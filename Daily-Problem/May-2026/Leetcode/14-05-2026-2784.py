# 2784. Check if Array is Good
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        seen = set()
        base_cnt_excd = False
        for num in nums :
            if num > n :
                return False
            if num in seen :
                if num < n or base_cnt_excd :
                    return False
                base_cnt_excd = True
            seen.add(num)
            
        
        return True
