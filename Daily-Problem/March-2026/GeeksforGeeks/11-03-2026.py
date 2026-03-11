# Sum of subarray minimums


class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        left_include = [0] * n
        right_include = [0] * n
        
        stack = []
        
        for i in range(n) :
            while stack and arr[stack[-1]] > arr[i] :
                stack.pop()
                
            left_include[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        
        while stack :
            stack.pop()
            
        for i in range(n-1,-1, -1) :
            while stack and arr[stack[-1]] >= arr[i] :
                stack.pop()
                
            right_include[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
            
        total_sum = 0
        for i in range(n) :
            total_sum =(total_sum +  (arr[i] * left_include[i] * right_include[i]))
            
        return total_sum
