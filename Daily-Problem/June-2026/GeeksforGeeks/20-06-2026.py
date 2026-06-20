# Last Digit of a^b

class Solution:
    def get_mod_value(self, a, b) :
        mod = 0
        n = len(b)
        
        for i in range(n) :
            mod = (mod * 10 + int(b[i])) % a
            
        return mod
    def getLastDigit(self, a, b):
        m = len(a)
        n = len(b)

        if m == 1 and a[0] == '0' :
            return 0
        
        if n == 1 and b[0] == '0' :
            return 1
            
        
        mod_value = self.get_mod_value(4, b)
        exp = 4 if mod_value == 0 else mod_value
        result = pow(int(a[m-1]) , exp)
        return result % 10
