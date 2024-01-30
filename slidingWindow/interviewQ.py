# largest sliding window 
'''
in this question , we're gonna keep adding teh next character
from the list to window as long as its larger than the current, if 
the next character is smaller than we make a new window

'''


def longest(string):
    #it is the starting window, so its gonna be 1 value long
    sub = string[0]
    long, length = sub, 1 # this will be the starting data 
    for i in string[1:]: #started at the first index cause we already looked
                        # at the 0th index element
        if sub[-1] <i :
            sub +=i
            if len(sub) >length:
                length  = len (sub)
                long = sub
            else:
                sub  = i
    print(long)

x = 'abcahdaabdtaafig'
longest(x)

