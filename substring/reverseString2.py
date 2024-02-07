

'''
https://leetcode.com/problems/reverse-string-ii/submissions/1169064590/
here we're gonna use a 2 pointer method
we're fist gonna convert the string into a list 
then we loop the list from start to end and step 2*k
the start pointer is initialized to 0
and the end pointer would be a min of the length of list and i+k-1 (i = current iteration , k = upto where we're trying to reverse list)
then we apply the basic 2 ptr method where keep going until the left is <  right 
and then swap the value at left with right and the right with left value, increment left and decrement right 
and then in the end print it in string form using ''.join(l)

'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)

        for i in range(0, len(l), 2*k):
            start = i
            end = min(i+k-1, len(l)-1)
            while start<end:
                l[start], l[end] = l[end], l[start]
                start+=1 
                end -=1
        return ''.join(l)