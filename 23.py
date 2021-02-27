#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER rows
#  2. INTEGER cols
#  3. INTEGER initR
#  4. INTEGER initC
#  5. INTEGER finalR
#  6. INTEGER finalC
#  7. INTEGER_ARRAY costRows
#  8. INTEGER_ARRAY costCols
#
from collections import deque

def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    # Write your code here
    move_cost = 0
    xx = [-1, 1, 0, 0]
    yy = [0, 0, -1, 1]
    visited = [[0 for __ in range(rows)] for _ in range(cols)]
    queue = deque([[initR, initC, move_cost]])
    cost_answer = 0
    
    while queue:
        q = queue.popleft()
        print(q[0], q[1], q[2])
        if q[0] == finalR and q[1] == finalC:
            cost_answer = q[2]
            break
        
        for i in range(4):
            qx = q[0] + xx[i]
            qy = q[1] + yy[i]
            if 0 <= qx < rows and 0 <= qy < cols:
                print(qx, qy)
                if visited[qx][qy] == 0:
                    visited[qx][qy] = 1
                    cost = 0
                    if i == 0 or i == 1:
                        cost = costRows[q[0]]
                    else:
                        cost = costCols[q[1]]
                    queue.append([qx, qy, q[2] + cost])
    
    return cost_answer

print([[0 for __ in range(81)] for _ in range(48)])