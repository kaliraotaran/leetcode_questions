

def bubble(list):
    index = len(list)-1
    sorted = False # we need it to break out of the loop after getting sorted list
    while True:
        sorted = True
        for i in range(0,index):
            if list[i]>list[i+1]:
                list[i], list[i+1]= list[i+1], list[i]
                sorted = False
    return list

print(bubble([4,3,5,1]))