# Pairs with Less Than K Diff
class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        n = len(arr)
        arr.sort()
        satisfied_pairs = 0
        left = 0
        right = 1
        
        while right < n :
            while left < right and (arr[right] - arr[left]) >= k :
                left += 1
            if left != right :
                satisfied_pairs += right - left
            right += 1
        
        return satisfied_pairs
