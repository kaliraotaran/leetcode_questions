
'''
https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75
'''


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 = {}
        hash2 = {}

        for i in nums1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] +=1
        
        for i in nums2:
            if i not in hash2:
                hash2[i]= 1
            else:
                hash2[i]+=1
        
        arr1 = []
        for keys, values in hash1.items():
            if keys not in hash2:
                arr1.append(keys)
        arr2 = []
        for keys, values in hash2.items():
            if keys not in hash1:
                arr2.append(keys)
        arr = [arr1]+[arr2]
        return arr

