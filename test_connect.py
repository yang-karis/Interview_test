# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 01:52:43 2019

@author: yumi3
"""
import numpy as np

test = np.array([[[1,1,1,0,0,0],
                 [1,1,0,1,0,0],
                 [1,0,1,0,0,0],
                 [0,1,0,1,1,0],
                 [0,0,0,1,1,1],
                 [0,0,0,0,1,1]],#1
                
                [[1,1,1,0,0,0],
                 [1,1,0,1,0,0],
                 [1,0,1,0,0,0],
                 [0,1,0,1,0,0],
                 [0,0,0,0,1,1],
                 [0,0,0,0,1,1]],#0
                 
                 [[1,0,1,0,0,0],
                  [0,1,1,1,1,0],
                  [1,1,1,1,0,0],
                  [0,1,1,1,0,0],
                  [0,1,0,0,1,0],
                  [0,0,0,0,0,1]],#0
                 
                 [[1,0,0,0,0,0],
                  [0,1,1,0,0,0],
                  [0,1,1,1,0,0],
                  [0,0,1,1,0,0],
                  [0,0,0,0,1,1],
                  [0,0,0,0,1,1]],#0
                 
                  [[1,1,0,0,0,0],
                   [1,1,1,0,0,0],
                   [0,1,1,1,0,0],
                   [0,0,1,1,0,0],
                   [0,0,0,0,1,1],
                   [0,0,0,0,1,1]],#0
                  
                  [[1,1,0,0,0,0],
                   [1,1,1,0,0,0],
                   [0,1,1,1,0,0],
                   [0,0,1,1,1,0],
                   [0,0,0,1,1,1],
                   [0,0,0,0,1,1]]])#1
  

np.save('test.npy',test)
  
  
  
  