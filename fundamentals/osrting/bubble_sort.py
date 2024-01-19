# Bubble sort is a simple sorting algorithm that works by repeatedly stepping 
# through the list element by element, comparing the current element with the 
# one after it, swapping their values if needed. These passes through the list
# are repeated until no swaps have to be performed during a pass, meaning that 
# the list has become fully sorted. The algorithm, which is a comparison sort, 
# is named for the way the larger elements "bubble" up to the top of the list.

def bubble(list):
    index = len(list)-1
    sorted = False # we need it to break out of the loop after getting sorted list
    while not sorted:
        sorted = True
        for i in range(0,index):
            if list[i]>list[i+1]:
                list[i], list[i+1]= list[i+1], list[i]
                sorted = False
    return list

print(bubble([4,3,5,1]))