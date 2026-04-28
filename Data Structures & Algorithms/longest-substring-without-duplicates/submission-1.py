class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        if not s:
            return 0
        res = 1
        merged = set()
        while right < len(s):
            merged.add(s[left])
            if s[right] not in merged:
                merged.add(s[right])
                res = max(res, len(merged))
                right += 1
            else:
                merged = set()
                left+= 1
                right = left + 1
            
        return res