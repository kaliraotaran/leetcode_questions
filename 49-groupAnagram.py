# https://leetcode.com/problems/group-anagrams/submissions/1129943121/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = [] 

        for s in strs:
            sorted_s = tuple(sorted(s)) # had to put it in a tuple cause after sorting, it gives a list as the result, which is an invalid key type for a hashmap
            anagram[sorted_s].append(s)
        
        for val in anagram.values():
            result.append(val)
        return result
ana = Solution()
print(ana.groupAnagrams(["eat", "tae", "tea", "bit", "tib", "tbt", "b53tt"]))