class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # res = 0
        # for i in range(len(s)):
        #     freq = {}
        #     maxf = 0
        #     for j in range(i, len(s)):
        #         freq[s[j]] = 1 + freq.get(s[j], 0)
        #         maxf = max(maxf, freq[s[j]])

        #         if (j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)

        # return res

        left = 0
        res = 0
        maxf = 0
        count_map = {}


        for right in range(len(s)):
            count_map[s[right]] = 1 + count_map.get(s[right], 0)
            maxf = max(maxf, count_map[s[right]])

            while (right - left + 1) - maxf > k:
                count_map[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


