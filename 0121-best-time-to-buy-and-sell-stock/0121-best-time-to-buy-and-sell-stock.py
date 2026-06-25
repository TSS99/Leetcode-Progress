class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Starting by assuming the first day is our lowest price
        minimum_price = prices[0]
        maximum_profit = 0
        
        # Iterating through the prices starting from the second day
        for i in range(1, len(prices)):
            # If a lower price would have found than our current minimum, update it
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            # Otherwise, check if selling today yields a better profit
            else:
                current_profit = prices[i] - minimum_price
                if current_profit > maximum_profit:
                    maximum_profit = current_profit
                    
        return maximum_profit