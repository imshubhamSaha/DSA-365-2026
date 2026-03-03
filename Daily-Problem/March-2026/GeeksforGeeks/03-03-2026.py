# Longest subarray with Atmost two distinct integers

class Solution:
    def totalElements(self, arr):
        n = len(arr)
        distinct = {}
        left = 0
        right = 0
        longest_length = 0
        while right < n :
            while len(distinct) == 2 and arr[right] not in distinct:
                distinct[arr[left]] = distinct[arr[left]] - 1
                if (distinct[arr[left]] == 0) :
                    distinct.pop(arr[left])
                left += 1
            distinct[arr[right]] = distinct.get(arr[right], 0) + 1
            longest_length = max(longest_length, (right - left) + 1)
            right += 1
        
        return longest_length
