# used to overcome the drawbacks of arrays



class Node:
    def __init__(self,data = None, next = None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self, data):
        node = Node(data, self.head) # we want the next element to be added at the head(at teh front)
        self.head = node # bascailly said that if a new node is inserted, it'll be the head
    
    def print(self):
        if self.head is None:
            return "Linked List is Empty"
        
        itr = self.head     # iterate(uses value of head to go to or iterate to next node)
        llstr = '' # linkedlist string

        while itr: # where there even is a head
            llstr += str(itr.data)+'-->'  # it'll print the current self.head's data
            itr = itr.next # it will iterate to the next ndoe 
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) # if the list is empty, we just add the node normally 
            return 
        
        itr = self.head
        while itr.next: # if there is another node after the current one
            itr = itr.next # then we keep moving forward till there is no node next to current one

        itr.next = Node(data, None) # after reaching the last element, we add teh new node

    def insert_values(self, data_list):# this is mostly used for inserting a list of values at once['bad','good','neutral']
        self.head = None # wiping out the current values
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr =itr.next
        return count
    
    def remove_at(self, index):
        if index< 0 or index >=self.get_length():
            raise IndexError("Index Out Of Range")
        if index ==0:
            self.head=self.head.next # this is if we want to remove the first element from the list
            return
        
        count =0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            raise IndexError("Index Out of range")
        if index ==0:
            self.insert_at_beg(data)
            return
        count=0
        itr = self.head
        while itr: 
            if count == index -1: # you also want to edit teh pointer of prev element
                node = Node(data, itr.next) # the next element would be the one where we're trying to insert the element
                itr.next = node
                break 

            itr = itr.next # simple loop to go thru all nodes in linked list
            count +=1
    
    def insert_after_value(self, data_after, data_to_insert): # insert a ndoe after a certain value
        if self.head == None:
            return 
        
        if self.head.value == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.next == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next



ll = LinkedList()
# ll.insert_at_beg(12)
# ll.insert_at_beg(43)
# ll.insert_at_end(1)
ll.insert_values(['good', 'bad','neutral'])
ll.remove_at(1)
ll.insert_at(1, 'new value')
ll.print()
print(ll.get_length())


