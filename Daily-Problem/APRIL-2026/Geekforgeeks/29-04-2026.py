# Min Swaps to Group 1s

class Solution:
    def minSwaps(self, arr):
        s = sum(arr)
        if s==0:
            return -1
        temp = sum(arr[0:s])
        mini = s-temp
        start=0
        for i in range(s,len(arr)):
            temp-=arr[start]
            temp+=arr[i]
            start+=1
            mini=min(mini,s-temp)
        return mini
