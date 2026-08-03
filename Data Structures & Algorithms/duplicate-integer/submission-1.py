class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_nums = set(nums)
        set_n = len(set_nums)
        return set_n!=n
        for i in range(n):
            a = nums[i]
            for j in range(n):
                b = nums[j]
                if i!=j and a==b: return True
        return False