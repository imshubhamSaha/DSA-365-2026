#Buy Stock with Transaction Fee

class Solution:
    def maxProfit(self, arr, k):
        n = len(arr)
        stock_holding = -arr[0]
        cash_holding = 0
        
        for i in range(1,n) :
            prev_cash_holding = cash_holding
            
            cash_holding = max(cash_holding, (stock_holding + arr[i] - k))
            stock_holding = max(stock_holding, (prev_cash_holding - arr[i]))
            
        return cash_holding
