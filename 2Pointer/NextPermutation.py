'''
https://leetcode.com/problems/next-permutation/
in this question ,we bascailly traverse the list from right to left 
and while traversing , if we encounter a number less than the current number, 
we then swap those numbers and that'll be the output
the output is the first swap that occurs
ex. [1,3,2]
    it goes from 2 to 3, the output is nothing becuase the value increaed not decreaed
    but when we go from 3 to 1, the value decreases, then we swap those values
    so the output will be [1,3,2] -> [3,1,2]
BUT
if the array is [3,2,1] the output is [1,2,3] because
'''