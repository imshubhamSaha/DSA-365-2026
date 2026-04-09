# Intersection of Two Sorted Arrays

class Solution:
    def intersection(self,a, b):
        n = len(a)
        m = len(b)
        index = 0
        idx = 0
        common_elements = []
        
        while (index < n) and (idx < m) :
            if a[index] == b[idx] :
                if (not common_elements or common_elements[-1] != a[index]) :
                    common_elements.append(a[index])
                index += 1
                idx += 1
            elif a[index] < b[idx] :
                index +=  1
            else :
                idx += 1
                
        return common_elements
        
