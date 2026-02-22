class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Added a safeguard for empty lists based on the description note
        if not prices:
            return 0
            
        buy_price = prices[0]
        profit = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            profit = max(profit, p - buy_price)
        return profit

# --- Test Cases ---
def run_tests():
    sol = Solution()

    # Test Case 1: Standard case with a clear profit
    # Buy at 1 (day 2), sell at 6 (day 5) -> Profit: 5
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test Case 1 Failed"

    # Test Case 2: Prices only go down (No profit possible)
    # Expected: 0
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0, "Test Case 2 Failed"

    # Test Case 3: Prices only go up 
    # Buy at 1, sell at 5 -> Profit: 4
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4, "Test Case 3 Failed"

    # Test Case 4: Single day (No transaction possible)
    # Expected: 0
    assert sol.maxProfit([5]) == 0, "Test Case 4 Failed"

    # Test Case 5: Empty list (Edge case)
    # Expected: 0
    assert sol.maxProfit([]) == 0, "Test Case 5 Failed"

    # Test Case 6: Buy and sell at the same price (Flat market)
    # Expected: 0
    assert sol.maxProfit([3, 3, 3, 3]) == 0, "Test Case 6 Failed"

    print("All test cases passed!")

run_tests()
