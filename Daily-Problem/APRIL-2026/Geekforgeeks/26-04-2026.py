#Common in 3 Sorted Arrays

class Solution:
    def commonElements(self, a, b, c):
        n1 = len(a)
        n2 = len(b)
        n3 = len(c)
        common = []
        
        i= j = k = 0
        
        while i < n1 and j < n2 and k < n3 :
            
            if (a[i] == b[j] == c[k]) :
                if not common or common[-1] != a[i] :
                    common.append(a[i])
                i += 1
                j += 1
                k += 1
            elif a[i] <= b[j] and a[i] <= c[k] :
                i += 1
            elif b[j] <= a[i] and b[j] <= c[k] :
                j += 1
            else :
                k += 1
                
        return common
