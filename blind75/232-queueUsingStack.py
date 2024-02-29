# https://leetcode.com/problems/implement-queue-using-stacks/submissions/1144440184/

class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = [] # we use 2 stack becasue when we add a value to list, it acts as stack and follows
            # the LIFO property, so using 2 stacks, we pop older value to s2 and later append them to s1 so that the older values are on top
        
    def push(self, x):

        while self.s1:  # moving older values to s2
            self.s2.append(self.s1.pop())

        self.s1.append(x) # adding new value
        while self.s2: # adding teh older value on top of the new value
            self.s1.append(self.s2.pop())

    def pop(self, ):
        return self.s1.pop()
    
    def peek(self):
        return self.s1[-1]
    def empty(self):
        return len(self.s1) == 0
    

# Your MyQueue object will be instantiated and called as such:
obj = Queue()
obj.push(12)
obj.push(22)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)