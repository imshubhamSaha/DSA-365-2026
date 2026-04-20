# 2078. Two Furthest Houses With Different Colors
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maximum_house_dist = 0
        first_house = colors[0]
        last_house = colors[n - 1]
        for i in range(n) :
            left_house = colors[i]
            right_house = colors[n-1-i]
            if (left_house != last_house) :
                maximum_house_dist = max(maximum_house_dist, abs(i - (n-1)))
            if right_house != first_house :
                maximum_house_dist = max(maximum_house_dist, abs(0 - (n - i - 1)))
        
        return maximum_house_dist
