class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        
        left = 0
        while left < (len(s2) - window + 1):
            count_map = {}

            while left < len(s2) and s2[left] not in freq:
                left += 1

            right = left + window

            for c in s2[left:right]:
                count_map[c] = 1 + count_map.get(c, 0)
            
            if count_map == freq:
                return True

            left += 1

        return False
