# https://leetcode.com/problems/valid-anagram/submissions/1129046037/


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # method 1
        # return Counter(s) == Counter(t) # here, it just counts the occurence of each letter with eachother and compares em

        # method 2
        # this is a more complicated version with the use of hashmaps

        # if len(s) != len(t): first filter is to check to see if their lenghts even match
        #    return False
        
        # countS, countT = {},{}

        # for i in range(len(s)):  here we created teh hashmaps
        #     countS[s[i]] = 1+countS.get(s[i], 0) we have to use zero because its one of the parameters of .get function
        #     countT[t[i]] = 1+countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c]!= countT.get(c, 0):
        #         return False
        # return True
    
        # method 3
        return sorted(s) == sorted(t)

sol = Solution()
isol = sol.isAnagram('tsaran', 'narat')
print(isol)