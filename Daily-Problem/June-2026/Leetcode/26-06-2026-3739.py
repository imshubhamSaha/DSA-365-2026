# 3739. Count Subarrays With Majority Element II
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        majority_cnt = [0] * (n * 2 + 1)
        majority_cnt[n] = 1
        idx = n
        majority_subarray = 0
        prefix_sum = 0

        for num in nums :
            if num != target :
                idx -= 1
                prefix_sum -= majority_cnt[idx]
                majority_cnt[idx] += 1
            else :
                prefix_sum += majority_cnt[idx]
                idx += 1
                majority_cnt[idx] += 1
            majority_subarray += prefix_sum

        return majority_subarray
