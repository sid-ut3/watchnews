# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:24:26 2018

@author: samba

"""

import scipy.stats
import numpy as np

data = {"0": {"Trump": [0.2, 0.5, 0.3, 0.1, 0.7, 0.9, 0.8, 0.9, 0.2, 0.9, 0.1, 0.9, 0.3, 0.9],
              "Macron": [0.7, 0.9, 0.8, 0.9, 0.2, 0.5, 0.3, 0.1, 0.2, 0.9, 0.5, 0.9, 0.3, 0.9]
              },
        "1": {"Trump": [0.5, 0.1, 0.2, 0.9, 0.2, 0.5, 0.3, 0.1, 0.8, 0.1, 0.9, 0.8, 0.9, 0.9],
              "Macron": [0.9, 0.9, 0.7, 0.9, 0.2, 0.5, 0.3, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1]
              }
        }


def moving_average(dataset, order):
    '''moving_average
    This function has two parameters:
        dataset : The values of the data to calculate their averages
        order : The order of the mobile average
    This function calculate de moving average of a data and return a moving average list
    '''
    ret = np.cumsum(dataset, dtype=float)
    ret[order:] = ret[order:] - ret[:-order]
    return ret[order - 1:] / order


def test_trend(data, word, id_day):
    '''trend
    This function has three parameters :
    data : json data
    word : words to analyse
    id_day :  day to analyse
    This function calculate the T-test for the means of two independent samples and returns the conclusion of the test
    '''
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day - 1])
    if(test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, 'Increasing_trend')
        elif (test[0] < 0):
            return(word, 'Decreasing_trend')
        else:
            return(word, 'No_trend')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Strongly_increasing_trend')
        elif (test[0] < 0):
            return(word, 'Strongly_decreasing_trend')
        else:
            return(word, 'No_trend')
    else:
        return(word, 'No_trend')


def polarity(data, val):
    '''polarity
    This function has two parameters :
    data : the data or json data
    val : The positive or negative part of the dictionary to be analyzed
    This function shows us the polarity of each word of the data with regard to the mobile average and the trend and return the conclusion of the test
    '''
    average_m = {}
    dict_data = {}
    result = {}
    for keys, values in data.items():
        if keys == val:
            dict_values = values
    for keys in dict_values.keys():
        average_m[keys] = moving_average(dict_values[keys], order=3)
        dict_data[keys] = [average_m[keys][0:6], average_m[keys][6:12]]
    for key in average_m.keys():
        word, conclude = test_trend(dict_data, key, 1)
        result[word] = conclude
    return result


def file_polarity(data):
    '''
    This function has one parameter :
    data : json data
    This function calls the function polarity and return json file with the word his polarity and his trend
    '''
    dict = {}
    for key in data.keys():
        dict[key] = polarity(data, key)
    return(dict)
test = file_polarity(data)
test
