class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_str = set(s1)

        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        window = len(s1)
        # right = 0
        # left = 0
        for i in range(len(s2)):
            
            count_map = {}
            res = 0
            
            if s2[i] in my_str:
                substr = s2[i: i + window]
                for c in substr:
                    count_map[c] = 1 + count_map.get(c, 0)
                left = 0
                while left < len(substr) and substr[left] in my_str and freq[s1[left]] == count_map[substr[left]]:
                    res += 1
                    left+=1
                if res == len(s1):
                    return True
        return False
