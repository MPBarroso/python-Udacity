# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:25:58 2020

@author: marco
"""
#import numpy as np
transposedata = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
#data = np.transpose(transposedata)
#data_transpose = # replace with your code
unzip = zip(*transposedata)
transpose_matrix = [list(row) for row in unzip]
print(transpose_matrix)