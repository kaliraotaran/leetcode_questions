class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        patternlist = list(pattern)
        slist = s.split()

        if len(patternlist) != len(slist):
            return False
        
        p_seen = {}
        s_seen = {}

        for i in range(len(patternlist)):
            if patternlist[i] in p_seen:
                if p_seen[patternlist[i]] != slist[i]:
                    return False
            else:
                p_seen[patternlist[i]] = slist[i]
            if slist[i] in s_seen:
                if s_seen[slist[i]]!=patternlist[i]:
                    return False
            else:
                s_seen[slist[i]] = patternlist[i]
        if len(p_seen) != len(s_seen):
            return False
        flag = True
        for i in range(len(pattern)):
            if p_seen[pattern[i]] != slist[i]:
                return False
        for i in range(len(slist)):
            if s_seen[slist[i]]!= pattern[i]:
                return False
        return True




        # hash1 = {}
        # hash2 = {}

        # for i in s:
        #     if i not in hash1:
        #         hash1[i] = 1
        #     else:
        #         if i in hash1:
        #             hash1[i]+=1
        # for i in pattern:
        #     if i not in hash2:
        #         hash2[i]=1
        #     else:
        #         if i in hash2:
        #             hash2[i]+=1
        # list1 = []
        # list2 = []
        # for values in hash1.values():
        #     list1.append(values)
        # for values in hash2.values():
        #     list2.append(values)
        # if list1.sort() == list2.sort():
        #     return True
        # else:
        #     return False