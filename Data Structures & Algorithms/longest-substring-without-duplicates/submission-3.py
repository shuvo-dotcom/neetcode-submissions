class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ls = 0
        vis = set()
        l, r = 0, 0
        while r<n:
            if s[r] not in vis:
                vis.add(s[r])
                ls = max(ls, r-l+1)
                r+=1
            else:
                vis.remove(s[l])
                l+=1
        return ls