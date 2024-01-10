# performs better than bubble sort because number of swaps is less

 
# Selection Sort works by dividing the input into two parts: the sorted sublist of items and the
#  unsorted sublist of the remaining items.

# During each iteration, the algorithm finds the smallest item in the unsorted sublist and moves
#  it to the end of the sorted sublist.

# This process continues until the unsorted sublist becomes empty and the sorted sublist contains 
# all the items in the original input.

# In each iteration, the algorithm uses the comparison operator to find the smallest item. It
#  then swaps that item with the last unsorted item in the array.

def selection(list):
    index = len(list)

    for i in range(0, index-1):
        minval = i
        for j in range(i+1, index):
            if list[j] <list[minval]:
                minval=j
        if minval != i:
            list[minval], list[i]= list[i], list[minval] # swapping w/o using temp variable
        print (minval)
    return list
print(selection([4,3,6,1,8,6]))