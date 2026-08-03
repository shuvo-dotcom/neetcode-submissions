class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parent_dict = {}
        m = len(strs)
        for k in range(m):
            s = strs[k]
            dict_s = ''.join(sorted(s))
            if dict_s in parent_dict: 
                parent_dict[dict_s].append(s)
            else: parent_dict[dict_s] = [s]
            
        return list(parent_dict.values())