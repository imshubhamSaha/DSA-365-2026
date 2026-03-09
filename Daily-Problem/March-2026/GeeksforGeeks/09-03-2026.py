# Largest number in one swap


class Solution:
    def largestSwap(self, s):
        n = len(s)
        last_freq = [-1] * 10
        number = []
        for i in range(n) :
            number.append(s[i])
            idx = ord(s[i]) - ord("0")
            last_freq[idx] = i
            
        for i in range(n) :
            swap_idx = -1
            num = ord(s[i]) - ord("0")
            for j in range(num+1, 10) :
                if last_freq[j] != -1 and last_freq[j] > i :
                    swap_idx = last_freq[j]
                    
            if swap_idx != -1 :
                temp = number[i]
                number[i] = number[swap_idx]
                number[swap_idx] = temp
                break
        
        return "".join(number)
        
