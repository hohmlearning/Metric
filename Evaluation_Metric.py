# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:34:10 2022

@author: Hohm
"""
import numpy as np

class Metric_regression():
    def fun_ARD (Y_exp, Y_calc):
        '''
        Calculates the Average Relative Deviation of the Experimental Data and the 
        fitted Data.
        '''

        datapoints = Y_exp.shape[0]
        epsilon = 1E-8
        non_zero = Y_exp > epsilon
        RD = np.zeros(Y_exp.shape)    
        RD[non_zero] = np.abs(Y_exp[non_zero] - Y_calc[non_zero]) / (Y_exp[non_zero] + epsilon)    
        RD_sum = RD.sum()    	  
        ARD = RD_sum/datapoints
       
        return (ARD)    
        
            
    def fun_R_square (self, Y_exp, Y_calc):
        '''
        Calculates the Residual sum of squares of two inputs.
        '''
        SSE = np.sum((Y_exp - Y_calc)**2) #SSE - Sum of Squared Errors
        y_1 = np.sum(Y_exp) / Y_exp.shape[0]
        SST = np.sum((y_1 - Y_exp)**2) #SST - Sum of Squares Total
        R_square = 1 - SSE / SST
        return (R_square)
    
    def fun_R_square_adj (self, Y_exp, Y_calc, dimension):
        '''
        Calculates the adjusted Residual sum of squares of two inputs.
    
        '''
        R_square =  self.fun_R_square (Y_exp, Y_calc)
        number_experimental_points = Y_exp.shape[0]
        R_adj = 1 - (number_experimental_points  - 1) / (number_experimental_points  - dimension) * (1 - R_square)
        return (R_adj)
    
    def fun_MSE (self, Y_exp, Y_calc):
        '''
        Calculates the Mean Squared Error.
        '''
        n = Y_exp.shape[0]
        MSE = np.power(Y_exp - Y_calc, 2) 
        MSE = np.sum(MSE) / n
        return (MSE)    
    
    def fun_RMSE (self, Y_exp, Y_calc):
        '''
        Calls fun_MSE and taked the square root of the Mean Squared Error.
        '''
        MSE = self.fun_MSE(Y_exp, Y_calc)
        RMSE = np.sqrt(MSE)
        return (RMSE) 

class Metric_classification():
    def fun_accurracy(self, Y_exp, Y_calc):
        '''
        The accuracy gives an overview over the model performance. Function available
        only if the classes are hard coded. Single mistakes are evaluated as 0 and  
        right predictions as 1. The function is then averaged. 
        Therefore, the accuracy is in range of 0 and 1. The accuracy is not
        meaningfull for inbalanced datasets.

        Parameters
        ----------
        Y_exp : Numpy vector (datapooints x 1)
        Y_calc : Numpy vector (datapooints x 1)

        Returns
        -------
        metric : float
        '''
        NB = Y_exp == Y_calc
        metric = NB.mean()
        return (metric)
    
    def fun_sensitivity_selecivity (self, y_exp, y_calc, class_label):
        '''
        Returns the sensitivity for class 1, if passed the corresponding
        class label. Besides, the selectivity is returned, if passed the
        class label of the second class.

        Parameters
        ----------
        y_exp :  Numpy vector (datapooints x 1)
        y_calc :  Numpy vector (datapooints x 1)
        class_label : integer [0, 1]

        Returns
        -------
        sensitivity : float [0, 1]

        '''
        positive_exp = y_exp == class_label 
        positive_calc = y_calc == class_label
        TP = (positive_exp * positive_calc).sum()
        TP_FN = positive_exp.sum()
        sensitivity = TP / TP_FN
        return (sensitivity)
    
    def fun_IoU (self, y_exp, y_calc, class_label):
        '''
        Calculates the Intersection over Union (IoU), or Jaccard Index,
        of the corresponding class.

        Parameters
        ----------
        y_exp : Numpy vector (datapooints x 1)
        y_calc : Numpy vector (datapooints x 1)
        class_label : integer [0, 1]

        Returns
        -------
        IoU : float [0, 1]

        '''
        positive_exp = y_exp == class_label 
        positive_calc = y_calc == class_label
        TP = (positive_exp * positive_calc).sum()
        IoU = TP / (positive_exp.sum() + positive_calc.sum() - TP)
        return (IoU)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
