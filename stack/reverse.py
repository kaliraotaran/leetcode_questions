
'''
this olution wont work on leetcode but when you run this program, it does 
reverse the string

'''
def reverse(s):
    
    stack = []
    for i in s:
        stack.append(i)
    strr = ''
    while stack:
        strr+= stack.pop()
    return strr

print(reverse('hello'))        