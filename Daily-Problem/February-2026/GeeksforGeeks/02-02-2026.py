# Max Circular Subarray Sum


class Solution:
    def maxCircularSum(self, arr):
        curr_min = curr_max = min_sum = max_sum = total_sum = arr[0]
        
        for i in range(1, len(arr)):
            curr_max = max(arr[i], curr_max + arr[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(arr[i], curr_min + arr[i])
            min_sum = min(min_sum, curr_min)

            total_sum += arr[i]

        if min_sum == total_sum:
            return max_sum
        return max(max_sum, total_sum - min_sum)
        