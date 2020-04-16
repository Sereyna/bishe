#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:39:58 2020

@author: sereyna
"""
import numpy as np

minint = 0
maxint = 50
dim = 10

map_carnum = np.random.randint(minint,maxint,(dim,dim))
map_carnum_filter = np.array(map_carnum)

for x in np.nditer(map_carnum_filter, op_flags=['readwrite']):
	if x < 30:
		x[...] = 0

