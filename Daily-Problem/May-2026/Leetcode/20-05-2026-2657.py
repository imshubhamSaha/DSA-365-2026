# 2657. Find the Prefix Common Array of Two Arrays
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        pc_arr = [0] * n

        matched = 0

        for i in range(n) :
            freq[A[i]] += 1
            freq[B[i]] += 1
            if A[i] == B[i] :
                matched += 1
            else :
                if (freq[A[i]] % 2) == 0 :
                    matched += 1
                if (freq[B[i]] % 2) == 0 :
                    matched += 1
            
            pc_arr[i] = matched

        return pc_arr
        
