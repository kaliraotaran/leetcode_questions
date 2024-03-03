'''
https://www.codingninjas.com/studio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=PROBLEM
'''



from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row = len(matrix)
    column = len(matrix[0])
    arri = []
    arrj = []



    for i in range(row):
        for j in range(column):
            if matrix[i][j]==0:
                arri.append(i)
                arrj.append(j)
    for rows in range(row):
        for cols in range(column):
            if (rows in arri or cols in arrj):
                matrix[rows][cols] = 0


    