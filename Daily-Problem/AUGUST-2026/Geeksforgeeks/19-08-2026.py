# Triplets with Sum in Range


class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        n = len(arr)
        arr.sort()
        count1=0
        count2=0
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                if arr[i]+arr[right]+arr[left]<=r:
                    count1+=(right-left)
                    left+=1
                else: 
                    right-=1
                    
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                if arr[i]+arr[left]+arr[right]<=l-1:
                    count2+=(right-left)
                    left+=1
                else:
                    right-=1
        return abs(count1-count2)
