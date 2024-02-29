# https://leetcode.com/problems/first-bad-version/description/

'''
here, we apply binary search
we have n updates or realeases and its bascially a list from 1-n
we have the isBadVersion(mid) func to tell us if teh veresion we're at is bad or not
if it is , then the new high is mid-1.
else its low = mid+1
the low value will be the answer not the mid value
'''



# The isBadVersion API is already defined for you in leetcode(not in this)
# def isBadVersion(version: int) -> bool: 
# (this is bascially binary search)
class Solution:
    def bad(self, n:int)->int:
        low = 0
        high = n
        
        while low<=high:
            mid = (low+high)//2 # first we get the middle point
            if isBadVersion(mid):
                high = mid -1 # if it's a bad version then we remove the left side
            else:
                low = mid + 1 # otherwise we move right from the mid
        return low
    

    # this is so i dont get the error(not the real isBadversion)
class isBadVersion:
    pass