class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        for s in strs:
            count = [0] * 26
            for i in range (len(s)):
                count[ord(s[i]) -  ord('a')] += 1
            
            if tuple(count) in group_map:
                group_map[tuple(count)].append(s)
            else:
                group_map[tuple(count)] = [s]
        res = []
        for _, value in group_map.items():
            res.append(value)

        return res