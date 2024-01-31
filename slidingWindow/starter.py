
'''
we are given a string and we have make a new subarray from the string, right when we encounter a letter with 
lesser value than prev. 
we then have to print the size of this sub array
'''

def longest(string):
    sub = string[0]
    long, length = sub, 1
    for i in string[1:]:
        if sub[-1] < i:
            sub+=i
            if len(sub)>length:
                length = len(sub)
                long = sub
        else:
            sub=i
        print(sub, long)
    print('the answer is', long)

y = 'abcahbaabdfgtaafigiz'
longest(y)