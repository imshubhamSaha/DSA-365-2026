# Last Moment Before All Ants Fall Out


class Solution:
    def getLastMoment(self, n, left, right):
        left_far_position = 0 if not left else max(left)
        right_least_position = n  if not right else min(right)
        
        return max(left_far_position, (n - right_least_position))