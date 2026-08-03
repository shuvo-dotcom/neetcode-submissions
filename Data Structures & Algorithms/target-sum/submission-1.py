class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def rec(indx, updated_target):
            if indx == n:
                if updated_target == target: return 1
                else: return 0
            positive = rec(indx+1, updated_target+nums[indx])    
            negative = rec(indx+1, updated_target-nums[indx])    
            return positive+negative
        return rec(0, 0)