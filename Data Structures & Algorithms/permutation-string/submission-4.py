class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)

        count_map = {}
        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        for c in s2[:len(s1)]:
            count_map[c] = 1 + count_map.get(c, 0)
        
        if count_map == freq:
            return True
        

        left = 0
        for right in range(window, len(s2)):
            count_map[s2[right]] = 1 + count_map.get(s2[right], 0)

            count_map[s2[left]] -= 1
            if count_map[s2[left]] == 0:
                del count_map[s2[left]]
            
            left += 1

            if count_map == freq:
                return True

        return False
        
        