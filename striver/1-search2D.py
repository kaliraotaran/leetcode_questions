'''
https://www.codingninjas.com/studio/problems/search-in-a-2d-matrix_980531?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''


def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.

    rows =len(mat)
    columns = len(mat[0])

    for i in range (rows):
        for j in range (columns):
            if mat[i][j] == target:
                return True
    return False