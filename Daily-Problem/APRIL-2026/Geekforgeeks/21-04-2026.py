# Two water Jug problem

class Solution:
    def my_gcd(self,a, b) :
        while b :
            temp = b
            b = a % b
            a = temp
        return a
    
    def pour_water(self,j1, j2, d) :
            first_jug = j1
            second_jug = 0
            steps_taken = 1
            
            while first_jug != d and second_jug != d :
                required_water = min(first_jug, j2 - second_jug)
                first_jug -= required_water
                second_jug += required_water
                steps_taken += 1
                
                if first_jug == d or second_jug == d :
                    return steps_taken
                
                if not first_jug :
                    first_jug = j1
                    steps_taken += 1
                
                if second_jug == j2 :
                    second_jug = 0
                    steps_taken += 1
                
            return steps_taken
        
	def minSteps(self, m, n, d):
	    if d > max(m,n) :
	        return -1
	        
		#GCD 
		GCD = self.my_gcd(m,n)
		if d % GCD :
		    return -1

        return min(self.pour_water(m, n, d), self.pour_water(n, m, d))
        
