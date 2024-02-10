

'''
https://leetcode.com/problems/defanging-an-ip-address/description/

here we simply  replace the "." with "[.]" in the input string, which is an IP address. 
so we iterate through the string and add a [.] to a new string if teh current letter in stirng is '.'
else we add the oeether characters to the newstring

'''

class Solution:
    def defang(self, address:str):

        res = ''

        for i in address:
            if i =='.':
                res+='[.]'
            else:
                res+=i
        return res