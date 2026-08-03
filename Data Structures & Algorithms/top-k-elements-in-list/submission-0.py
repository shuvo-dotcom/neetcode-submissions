class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]] = 1
            else: dict_nums[nums[i]] += 1

        nums_tuple = list()
        
        for j in dict_nums.keys():
            nums_tuple.append((dict_nums[j], j))
        updated_tuple = sorted(nums_tuple, reverse=True)
        res = []
        for k in range(k):
            res.append(updated_tuple[k][1])
        return res