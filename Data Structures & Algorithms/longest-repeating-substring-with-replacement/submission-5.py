class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0

        most_freq = 0
        counts = {}
        for right in range(len(s)):

            counts[s[right]] = counts.get(s[right], 0) + 1

            most_freq = max(most_freq, counts[s[right]])

            while (right - left + 1) - most_freq > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
