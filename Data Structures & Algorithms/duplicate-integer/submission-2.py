class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_nums = set(nums)
        set_n = len(set_nums)
        return set_n!=n