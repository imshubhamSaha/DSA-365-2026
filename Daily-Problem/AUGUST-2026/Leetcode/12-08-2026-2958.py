# 2958. Length of Longest Subarray With at Most K Frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        max_subarray_length = 0
        freq_mpp = {}
        while right < n :
            freq_mpp[nums[right]] = freq_mpp.get(nums[right], 0) + 1

            while left < right and freq_mpp[nums[right]] > k :
                freq_mpp[nums[left]] -= 1
                if freq_mpp[nums[left]] == 0 :
                    del freq_mpp[nums[left]]
                left += 1

            max_subarray_length = max(max_subarray_length, (right - left) + 1)
            right += 1
        
        return max_subarray_length
