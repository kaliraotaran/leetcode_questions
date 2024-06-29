

'''
https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75 
'''



class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}
        
        for i in arr:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] +=1
        
        arr1 = []
        for keys, values in hash.items():
            if values not in arr1:
                arr1.append(values)
            else:
                return False
        return True