# Count Pairs Divisible By K


class Solution:
    def countKdivPairs(self, arr, k):
        ans = 0
        freq = [0] * k
        
        for num in arr:
            rem = num % k
            complement = (k - rem) % k
            
            ans += freq[complement]
            freq[rem] += 1
            
        return ans   
