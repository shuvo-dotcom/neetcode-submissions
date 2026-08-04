class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while r > l:
            a = numbers[l]
            b = numbers[r]
            if a+b > target: r-=1
            elif a+b < target: l+=1
            else: return [l+1, r+1]