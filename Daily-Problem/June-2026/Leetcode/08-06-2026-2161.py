#2161. Partition Array According to Given Pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for num in nums :
            if num < pivot :
                result[left] = num
                left += 1
        for i in range (n-1, -1, -1) :
            if nums[i] > pivot :
                result[right] = nums[i]
                right -= 1
            elif nums[i] == pivot :
                result[left] = pivot
                left += 1
        

        return result

  ----------------------------

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        j = n - 1
        for num in nums :
            if num < pivot :
                result[left] = num
                left += 1
            if nums[j] > pivot :
                result[right] = nums[j]
                right -= 1
            j -= 1
        
        while left <= right :
            result[right] = pivot
            right -= 1
        
        return result
        

        return result
