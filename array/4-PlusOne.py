
'''
https://leetcode.com/problems/plus-one/submissions/1279782285/
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''
        for i in digits:
            str1+=str(i)## first i got every integer from the array and turned each of them into a 
                    # string and added them to the str1 string

        # then i turned the string i made from the intergers from the array into an interger itself
        int1 = int(str1)
        # i then added 1 to that new interger that i made
        int1+=1

        # then i turned that new interger back into a string
        str2 = str(int1)

        
        arr2 = []
        # then i added every single letter from the string back into an interger and added it to the array
        for i in str2:  
            arr2.append(int(i))

        return arr2
    

