class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProf = prices[0], 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProf:
                maxProf = price - minPrice
        return maxProf
            