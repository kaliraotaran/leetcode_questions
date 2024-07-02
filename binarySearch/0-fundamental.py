

def binary(list1, n):
    low =0
    high = len(list1)-1
    mid =0

    while low<=high:

        mid = (high+low)//2
        if list1[mid]==n:
            return mid
        elif list1[mid] > n:
            high = mid-1
        else:
            low = mid+1
    return -1
