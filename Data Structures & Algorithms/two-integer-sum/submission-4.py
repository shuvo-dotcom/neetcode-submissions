class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        pos = {}
        for j in range(n):
            if nums[j] not in pos:    
                pos[nums[j]] = [j]
            else:
                pos[nums[j]].append(j)

        for i in range(n):
            remaining_sum = target-nums[i]
            if remaining_sum == nums[i]:
                if len(pos[remaining_sum]) > 1: return pos[remaining_sum]
            else:
                if remaining_sum in pos:
                    return [pos[nums[i]][0], pos[remaining_sum][0]]
        return