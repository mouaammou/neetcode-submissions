class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        
        for i in range(len(s2) - window + 1):
            count_map = {}

            substr = s2[i: i + window]

            for c in substr:
                count_map[c] = 1 + count_map.get(c, 0)
            
            if count_map == freq:
                return True
        return False
