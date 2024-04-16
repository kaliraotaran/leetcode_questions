

'''
https://leetcode.com/problems/isomorphic-strings/submissions/1234212343/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hashs = {}
        # hasht = {}

        # for i in s:
        #     if i not in hashs:
        #         hashs[i] =1
        #     else:
        #         hashs[i] +=1
        # for i in t:
        #     if i not in hasht:
        #         hasht[i] =1
        #     else:
        #         hasht[i]+=1
        # if hashs  != hasht :
        #     return False
        # else:
        #     return True

        list1 = []
        list2 = []
        for i in s:
            list1.append(s.index(i))
        for i in t:
            list2.append(t.index(i))
        if list1 == list2:
            return True
        else:return False