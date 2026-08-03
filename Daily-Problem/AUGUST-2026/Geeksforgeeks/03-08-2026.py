# Max Sum Subarray of Size at least K

class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        j = 0
        running_sum = 0
        last = 0
        max_sum = float('-inf')
        for i in range(n) :
            running_sum = running_sum + arr[i]
            if (i-j+1) == k :
                max_sum = max(max_sum,running_sum)
            elif (i-j+1) > k :
                max_sum = max(max_sum,running_sum)
                last += arr[j]
                j += 1
                if last < 0 :
                    running_sum -= last
                    max_sum = max(max_sum,running_sum)
                    last = 0
    
        return max_sum
        
