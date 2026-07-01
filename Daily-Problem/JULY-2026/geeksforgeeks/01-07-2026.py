# Max Subarray Sum by Removing At Most One

class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)
        curr_sum = max_sum = arr[0]
        skipped_sum = 0
        for i in range(1, n):
            skipped_sum = max(curr_sum, skipped_sum + arr[i])
            curr_sum = max(curr_sum + arr[i], arr[i])
            max_sum = max(max_sum, curr_sum, skipped_sum)
        return max_sum
