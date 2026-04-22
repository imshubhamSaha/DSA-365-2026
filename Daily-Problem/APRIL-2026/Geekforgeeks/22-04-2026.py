#Mean of range in array

class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        q = len(queries)
        avg_mean = [0] * q
        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]
        
        for i in range(1, n) :
            prefix_sum[i] = arr[i] + prefix_sum[i-1]
            
        for i in range(q) :
            start, end = queries[i]
            avg_mean[i] = (arr[start] + (prefix_sum[end] - prefix_sum[start])) // (end - start + 1)
        
        return avg_mean
