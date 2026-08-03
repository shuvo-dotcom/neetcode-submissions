class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sums = sum(nums)
        dp = [[None] * (2 * total_sums + 1) for _ in range(n)]
        def rec(indx, updated_target, dp):
            if indx == n:
                if updated_target == target: return 1
                else: return 0
            shifted_target = updated_target + total_sums

            if dp[indx][shifted_target] is not None:
                return dp[indx][shifted_target]
            positive = rec(indx+1, updated_target+nums[indx], dp)    
            negative = rec(indx+1, updated_target-nums[indx], dp)   
            dp[indx][shifted_target] = positive+negative
            return dp[indx][shifted_target]
        return rec(0, 0, dp)