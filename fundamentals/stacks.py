# LIFO
# inpython we can use list as a stack

session = []
session.append(3)# keeps adding elements to the top of the list
session.append(4) 

last = session.pop() # this takes out the last added element in the list

# print(session)

if not session:
    session[-1]


# using a deque as a stack
    
from collections import deque
stack = deque()

dir(stack) # this will tell me aboput all methods of deque

stack.append(23)
stack.append(33)
stack.append(43)
# print(stack)


# reverse a string using a stack
string=[]
def reverse(s):
    for i in s:
        string.append(i)
    string2 =''
    for i in range(len(string)):
        string2 +=(string.pop())
    print(string2)
# reverse('we will conquer covid-19')

# balanced paranthesis
    
def match(c1, c2):
    matchval = {
        '}' : '{',
        ']' : '[',
        ')' : '(',
    }
    return matchval[c1] == c2

def balanced(s):
    stack = []
    for c in s:
        if c=='{' or c=="[" or c=='(':
            stack.append(c)
        if c=='}' or c==']' or c==')':
             if len(stack) ==0:
                 return False
             if not match(c, stack.pop()):
                 return False
    return len(stack) ==0

print(balanced('[]{'))