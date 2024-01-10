# we sort the list using the pivot element

def quick(list):
    length = len(list)

    if length <=1:
        return list
    else:
        pivot = list.pop() # we assign the last elemnt oflist to pivot
    
    item_greater = []
    item_lower = []
    
    for item in list:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    return quick(item_lower)+[pivot]+quick(item_greater)


print(quick([4,3,5,2,7,1,8,9,8]))