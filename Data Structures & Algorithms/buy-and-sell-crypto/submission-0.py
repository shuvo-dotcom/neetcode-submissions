class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l = len(nums)
        max_profit = 0
        for i in range(l):
            buy = nums[i]
            for j in range(i+1, l):
                sell = nums[j]
                profit = sell - buy
                max_profit = max(profit, max_profit)
        return max_profit