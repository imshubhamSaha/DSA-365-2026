# Substring with Max Zero-One Diff

class Solution:
	def maxSubstring(self, s):
		n = len(s)
		no_zeros = 0
		max_diff = -1
		
		for num in s :
		    if num == '1' :
		        no_zeros -= 1
		    elif num == '0' :
		        no_zeros += 1
		    max_diff = max(max_diff, no_zeros)
		    if no_zeros < 0 :
		        no_zeros = 0
		
		return max_diff if max_diff != 0 else -1
		
		
		
