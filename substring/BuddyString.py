'''
https://leetcode.com/problems/buddy-strings/solutions/3710426/beat-s-100-c-java-python-beginner-friendly/

we'll first check if both the string are equal, if they are-    
    -we store the s string in a set(remove duplicate characters)
    - then we compare the len of the set and the goal string

we then create 2 variables initilized to 0 and last element of the list
we then create 2 different while loops that apply operation to both the pointers
while the  pointer i is less than j and the current character at index i of s is equal to the ith vaule at goal, 
        then we increment i by 1
while j >=0 and the value at j in s is equal to value at j in goal:
        then we decrement j by 1
    
if the value of i is still less than j
    we create a list out of s
    then we swap values of i and j in the new list of s
    and then in the end, we convert teh list back to a string


'''


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        
        if len(goal) != n:
            return False
        
        if s ==goal:
            temp = set(s)
            return len(temp)<len(goal)

        i = 0
        j = n-1

        while i <j and s[i] ==goal[i]:
            i+=1
        while j >=0 and s[j] == goal[j]:
            j-=1
        
        if i<j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)
        return s ==goal