# Maximize Number of 1's


class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        flipped = 0
        max_consecutive = 0
        left = 0
        right = 0

        while right < n:
            if arr[right] == 0:
                flipped += 1
            while left <= right and flipped > k:
                if arr[left] == 0:
                    flipped -= 1
                left += 1

            max_consecutive = max(max_consecutive, (right - left) + 1)

            right += 1

        return max_consecutive
