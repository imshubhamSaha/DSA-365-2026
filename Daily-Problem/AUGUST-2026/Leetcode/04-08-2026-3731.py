# 3731. Find Missing Elements
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        smallest = nums[0]
        largest = nums[n-1]
        missing = []
        idx = 0
        for i in range(smallest, largest + 1) :
            if i != nums[idx] :
                missing.append(i)
            else : 
                idx += 1

        return missing
        
    
