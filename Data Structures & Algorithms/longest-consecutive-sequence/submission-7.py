class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums)
        ls = 0
        for nums_elem in nums_set:

            if nums_elem - 1 not in nums_set:
                length = 1
                while length + nums_elem in nums_set:
                    length += 1
            
                ls = max(length, ls)
        return ls