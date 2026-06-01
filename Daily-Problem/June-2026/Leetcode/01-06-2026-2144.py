# 2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        total_cost = 0
        cost.sort()

        for i in range(n - 1, -1, -3) :
            if i == 0 :
                total_cost += cost[i]
            else :
                total_cost += cost[i] + cost[i-1]
        
        return total_cost
