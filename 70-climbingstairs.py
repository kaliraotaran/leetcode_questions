# https://leetcode.com/problems/climbing-stairs/submissions/1139693594/
'''
this is sorta like the fibb series, we first take an initial list with 2 1's ,
we then add the last 2 elements in the list for n times (in a while loop) for i times and we increment i by one every time
then we print the last element in the list,
'''
class Solution:
    def climb(self, n:int)->int:
        buf = [1,1]
        i=0

        while i<n-1:
            buf.append(buf[-1]+buf[-2]) # we keep adding the last 2 elements in the list
            i+=1
        return buf[n] # the last element will be the one that tells teh total diffrent combinations of n
print(Solution().climb(5))