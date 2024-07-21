
'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        hash = Counter(nums)
        
            
        arr = []
        for keys, values in hash.items():
            arr.append((values, keys))

        arr.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
        