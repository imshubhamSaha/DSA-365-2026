# Construct List using XOR Queries


class Solution:
    def constructList(self, queries):
        n = len(queries)
        xor = 0
        xor_arr = [0] * n
        for i in range(n-1, -1, -1) :
            iden, val = queries[i]
            if iden == 1 :
                xor ^= val 
            xor_arr[i] = xor
                
        result = []
        result.append(xor)
        
        
        for i in range(n) :
            iden, val = queries[i]
            if iden == 0 :
                result.append(val ^ xor_arr[i])
        
        result.sort()
        return result
  ---------------------------


class Solution:
    def constructList(self, queries):
        n = len(queries)
        xor = 0
        for i in range(n) :
            iden, val = queries[i]
            if iden == 1 :
                xor ^= val 
                
        result = []
        result.append(xor)
        
        
        for i in range(n) :
            iden, val = queries[i]
            if iden == 0 :
                result.append(val ^ xor)
            else :
                xor ^= val
        
        result.sort()
        return result
        

