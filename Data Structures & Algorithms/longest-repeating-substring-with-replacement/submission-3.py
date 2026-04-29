class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        for i in range(len(s)):
            freq = {}
            maxf = 0
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq.get(s[j], 0)
                maxf = max(maxf, freq[s[j]])

                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)

        return res


