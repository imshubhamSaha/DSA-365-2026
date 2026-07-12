# 1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0 :
            return []
        dup_arr = [0] * n
        for i in range(n) :
            dup_arr[i] = arr[i]

        dup_arr.sort()
        mpp = {}
        mpp[dup_arr[0]] = 1

        for i in range(1, n) :
            if dup_arr[i] > dup_arr[i-1] :
                mpp[dup_arr[i]] = mpp[dup_arr[i-1]] + 1
        
        result = []

        for num in arr :
            result.append(mpp[num])
        
        return result
