class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0

        result = 0
        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            elif price - low > result:
                result = price - low

        return result


sol_121 = Solution()

# Test cases for 121. Best Time to Buy and Sell Stock
print(sol_121.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(sol_121.maxProfit([7, 6, 4, 3, 1]))    # Expected: 0
print(sol_121.maxProfit([1, 2]))             # Expected: 1
print(sol_121.maxProfit([]))                 # Expected: 0