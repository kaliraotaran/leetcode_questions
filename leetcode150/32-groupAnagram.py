'''
https://leetcode.com/problems/group-anagrams/submissions/1239221554/?envType=study-plan-v2&envId=top-interview-150

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for words in strs:
            temp = ''.join(sorted(words))
            if temp in hash:
                hash[temp].append(words)
            else:
                hash[temp] = [words]
        return hash.values()