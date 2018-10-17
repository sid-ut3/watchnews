import scipy.stats
import json
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:29:08 2018

@author: samba
"""
""" Trend second version """

with open('C:/Users/samba/Groupe8_Analyse_tendance/Data/Test/jour.json', 'r') as file:
    data = json.load(file)


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


def file_trend(data):
    """ data preprocessing for groupe 9
    param : file -> json file
    return json with trend, period and most important word"""
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1, len(valeur)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)


""" Test  """
trend = file_trend(data)
