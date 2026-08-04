class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            a = nums[i]
            l = i+1
            r = n-1
            while r>l:
                b = nums[l]
                c = nums[r]
                if a+b+c == 0: 
                    if [a, b, c] not in res:
                        res.append([a, b, c])
                    l+=1
                    r-=1
                elif a+b+c > 0:
                    r-=1
                else: l+=1
                    


        return res
            