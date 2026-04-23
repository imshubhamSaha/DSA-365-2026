#2615.Sum of Distances
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx_group = {}

        for i in range(n) :
            num = nums[i]
            if num not in idx_group:
                idx_group[num] = []
            idx_group[num].append(i)

        arr = [0] * n

        for num in idx_group :
            val_idx = idx_group[num]
            m = len(val_idx)

            prefix_sum = [0] * m
            prefix_sum[0] = val_idx[0]
            for i in range(1,m) :
                prefix_sum[i] = prefix_sum[i-1] + val_idx[i]

            for i in range(m) :
                left_dist_sum = i * val_idx[i] - prefix_sum[i-1] if i > 0 else 0
                right_dist_sum = (prefix_sum[m - 1] - prefix_sum[i]) - (m - i - 1) * val_idx[i] 
                arr[val_idx[i]] = left_dist_sum + right_dist_sum
        
        return arr
 
