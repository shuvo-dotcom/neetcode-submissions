class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(n):
                b = nums[j]
                if i!=j and a+b == target: return [i,j]
        return