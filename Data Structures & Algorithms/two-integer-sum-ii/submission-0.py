class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            a = numbers[i]
            for j in range(n):
                b = numbers[j]
                if i!=j and a+b == target: return [i+1, j+1]