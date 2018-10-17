"""

inter-promo project
group n°8

author: nicolas paillier

this program aims:
    - to apply a linear regression ; ie. to calculate the coefficient and
        the intercept value of the regression line

"""



"""

packages

"""

import numpy as np

from statsmodels.api import OLS



"""

functions

"""

def linear_regression(data):
    """
    goal of this function :
        - to apply a linear regression ; ie. to calculate the coefficient and
        the intercept value of the regression line
    input parameter :
        - json file's content (data)
    output :
        - dict containing the coefficient value and intercept for each word
    cmd packages :
        - numpy (ones, arange)
        - statsmodels.api (ols)
    """
    
    #initialisation
    dict_linreg = {}
    
    #for each entry in the json file (data)
    #intercept value and coefficient calculation
    for k, v in data.items():
        mat_x = np.ones((len(v), 2))
        mat_x[:,1] = np.arange(0, len(v))
        
        reg = OLS(v, mat_x)
        results = reg.fit()
        
        dict_linreg[k] = [results.params[1], results.params[0]]

    return(dict_linreg)