class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            tmp = 1
            for j in range(n):
                if i==j: continue
                else: tmp *=nums[j]
            res.append(tmp)
        return res