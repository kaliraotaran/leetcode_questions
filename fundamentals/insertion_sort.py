# not a fast sorting algo casue it need nested for loops
 

def insertion(list):
    n = len(list)
    for i in range(1, n):
        valuetosort = list[i]

        while list[i-1]> valuetosort and i>0:
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1
    return list

print(insertion([4,5,3,7,6,1,2]))