class Solution:
      def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {''.join(sorted(item)): [] for item in (strs)}
        for item in strs:
            sorted_s = ''.join(sorted(item))
            my_map[sorted_s].append(item)

        return list(my_map.values())
            