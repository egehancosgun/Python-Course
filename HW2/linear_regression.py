#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 02:45:46 2021

@author: egehancosgun
"""

import pandas as pd
import numpy as np
import scipy.stats as st
import scipy 

def linear_regression_function(x, y):
    
    nan_indices_x = x[x.iloc[:,-1].isnull()].index.tolist()
    nan_indices_y = y[y.iloc[:,-1].isnull()].index.tolist()
    
    nan_indices = list(set(nan_indices_x + nan_indices_y))
    
    x.drop(nan_indices, inplace = True)
    y.drop(nan_indices, inplace = True)
    
    x = np.array(x)
    y = np.array(y)
    
    n = np.size(x) 
    x_mean = np.mean(x)
    y_mean = np.mean(y) 
    sample_cov_xy = np.sum(x * y) - (x_mean * y_mean) * n
    sample_var_x = np.sum(x ** 2) - (x_mean ** 2) * n

    beta= sample_cov_xy / sample_var_x
    alpha = y_mean- beta * x_mean
    y_pred = alpha + beta * x	
    
    residuals = (y - y_pred) ** 2
    standard_error = np.sqrt(residuals.sum() / len(x))
    
    t_stat = scipy.stats.t.ppf(0.975, n-2)

    confidence_upper = y_pred + t_stat * standard_error
    confidence_lower = y_pred - t_stat * standard_error
    
    return (y_pred, alpha, beta, residuals, confidence_lower, confidence_upper)
