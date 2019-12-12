class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            # Find maximum between maxProfit and profit = p - minPrice
            # Solution 1
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(p, minPrice)

            # Solution 2
            # if p < minPrice:
            #     minPrice = p
            # elif p - minPrice > maxProfit:
            #     maxProfit = p - minPrice
        return maxProfit