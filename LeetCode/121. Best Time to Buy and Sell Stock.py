# my solution - so slow
# dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_dp = [prices[0]]+[10**4]*(len(prices)-1)
        for i in range(1, len(prices)):
            min_dp[i] = min(min_dp[i-1], prices[i])
             
        max_dp = [0]*(len(prices)-1)+[prices[-1]]
        for i in range(len(prices)-2, -1, -1):
            max_dp[i] = max(max_dp[i+1], prices[i])
            
        result = 0
        for p1, p2 in zip(min_dp, max_dp):
            result = max(result, p2-p1)
        return result

# another solution
# more readable and fast
def maxProfit(self, prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit