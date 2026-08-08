from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n: return []
        l, maxi, tracker = 0, [], deque()
        for r in range(n):
            while tracker and nums[r] >= nums[tracker[-1]]:
                tracker.pop()
            tracker.append(r)
            if tracker[0]<l: tracker.popleft()
            if r-l+1 == k:
                maxi.append(nums[tracker[0]])
                l+=1
        return maxi
