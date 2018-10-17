# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:55:43 2018

@author: valentin
@groupe : 8
"""
import scipy
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf
import numpy as np

data_add = {
    "mot1": [
        10,
        11,
        15,
        12,
        13,
        18,
        15,
        19,
        25,
        50,
        75,
        90,
        100,
        110],
    "macron": [
        17,
        15,
        14,
        15,
        13,
        12,
        10,
        9,
        9,
        8,
        8,
        7,
        8,
        6,
        5,
        4,
        3,
        2]}
data_mult = {"test":[10, 11, 15, 12, 13, 18, 15, 100, 110, 150, 120, 130, 180, 150]}
data_add2 = [10, 11, 15, 12, 13, 18, 15, 10, 11, 15, 12, 13, 18, 15]
data_mult = {
    "mot1": [
        0,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31,
        10,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31]}
data_test = [
    0,
    11,
    15,
    12,
    13,
    18,
    15,
    100,
    110,
    150,
    120,
    130,
    180,
    150,
    15,
    14,
    15,
    14,
    18,
    19,
    20,
    205,
    260,
    280,
    14,
    18,
    16,
    14,
    25,
    28,
    31,
    10,
    11,
    15,
    12,
    13,
    18,
    15,
    100,
    110,
    150,
    120,
    130,
    180,
    150,
    15,
    14,
    15,
    14,
    18,
    19,
    20,
    205,
    260,
    280,
    14,
    18,
    16,
    14,
    25,
    28,
    31]
data_mult2 = {
    "mot1": [
        0,
        11,
        15,
        12,
        13,
        18,
        15,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        15,
        14,
        15,
        14,
        18,
        19,
        20,
        205,
        260,
        280,
        14,
        18,
        16,
        14,
        25,
        28,
        31,
        100,
        110,
        150,
        120,
        130,
        180,
        150,
        1000,
        1100,
        1500,
        1200,
        1300,
        1800,
        1500,
        150,
        140,
        150,
        140,
        180,
        190,
        200,
        2050,
        2600,
        2800,
        140,
        180,
        160,
        140,
        250,
        280,
        310]}

res = sm.tsa.seasonal_decompose(data_test,
                                freq=31,
                                model='multiplicative')
sm.tsa.seasonal_decompose

res.resid
<<<<<<< HEAD

=======
>>>>>>> 5800095a83a43fd2b2795db8fd3424f7cb2cc329

def trend_by_period(data, interest_period):
    '''To get the trend of time series
    param : data -> dictionary of list of values (tf values)
    in chronological order by word
    interest_period -> integer, number of day by period
    7 for week, 31 for month
    period : month, week. Use to add residual values
    return list of dictionary wich contains trend and word
    '''

    list_data = []
    result_trend = []
    for key, val in data.items():
        preprocess = {"values": val, "word": key}
        list_data.append(preprocess)
    # first step : check if the model is addive or multiplicative
    for i in range(len(list_data)):
        if 0 in list_data[i]["values"]:
            res_additive = sm.tsa.seasonal_decompose(
                    list_data[i]["values"], freq=interest_period, model='additive')
            if interest_period == 7:
                trend_values = {list_data[i]["word"]: [
                                res_additive.trend[3:6], res_additive.trend[7:10]]}
                test_trend = file_trend(trend_values)
            #else:
                #trend_values = {list_data[i]["word"]: [
                                #res_additive.trend[15:31], res_additive.trend[32:47]]}
                #test_trend = file_trend(trend_values)
            #print(test_trend)
        else:
            res_additive = sm.tsa.seasonal_decompose(
                    list_data[i]["values"], freq=interest_period, model='additive')
            res_multiplicative = sm.tsa.seasonal_decompose(
                    list_data[i]["values"], freq=interest_period, model='multiplicative')
    # recover residual by model
            if interest_period == 7:
                residual_additive = res_additive.resid[3:11]
                residual_multiplicative = res_multiplicative.resid[3:11]
    # get autocorrelation values of the residual by model
                cor_add = acf(residual_additive)
                cor_mult = acf(residual_multiplicative)
    # Choose model type (additive or multiplicative)
                if sum(residual_additive) != 0:
                    if sum(cor_add**2) >= sum(cor_mult**2):
                        print('additive')
                    # use t_test to detect trend
<<<<<<< HEAD
                    trend_values = {list_data[i]["word"]: [
                        res_additive.trend[3:6], res_additive.trend[7:10]]}
                    test_trend = file_trend(trend_values)
                    print("----------------------")
                    print(trend_values)
=======
                        trend_values = {list_data[i]["word"]: [
                                res_additive.trend[3:6], res_additive.trend[7:10]]}
                        test_trend = file_trend(trend_values)
                        print(trend_values)
                    else:
                        sum(cor_mult**2)
                        trend_values = {list_data[i]["word"]: [
                                res_multiplicative.trend[3:6], res_multiplicative.trend[7:10]]}
                        test_trend = file_trend(trend_values)
                        print(trend_values)
>>>>>>> 5800095a83a43fd2b2795db8fd3424f7cb2cc329
                else:
                    test_trend = {list_data[i]["word"]: 'Pas_de_Tendance'}
            else:
                residual_additive = res_additive.resid[15:46]
                residual_multiplicative = res_multiplicative.resid[15:46]
                if sum(residual_additive) != 0:
                    cor_add = acf(residual_additive)
                    cor_mult = acf(residual_multiplicative)
                    if sum(cor_add**2) >= sum(cor_mult**2):
                        trend_values = {list_data[i]["word"]: [
                                res_additive.trend[15:31], res_additive.trend[32:47]]}
                        test_trend = file_trend(trend_values)
                    else:
                        print('mult')
                        trend_values = {list_data[i]["word"]: [
                                res_multiplicative.trend[15:31], res_multiplicative.trend[32:47]]}
                        test_trend = file_trend(trend_values)
                else:
                    test_trend = {list_data[i]["word"]: 'Pas_de_Tendance'}
        result_trend.append(test_trend)
    return result_trend


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
            return(word, 'Tendance_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    elif(test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, 'Tendance_fortement_en_hausse')
        elif (test[0] < 0):
            return(word, 'Tendance_fortement_en_baisse')
        else:
            return(word, 'Pas_de_Tendance')
    else:
        return(word, 'Pas_de_tendance')

data_bis = { data_bis = {"trump" : [0, 1, 1, 3, 2, 4, 5, 5, 6, 8, 7, 9, 11, 10], "macron" : [17, 15, 14, 15, 13, 12, 10, 9, 9, 8, 8, 7, 8, 6], "ceremonie" : [0, 0, 2, 1, 3, 4, 5, 6, 6, 5, 4, 4, 3, 3], "aeroport" : [3, 3, 2, 3, 3, 4, 2, 2, 4, 3, 3, 3, 4, 4], "tempete" : [5, 5, 5, 4, 5, 4, 4, 5, 5, 6, 6, 5, 5, 4], "impot" : [20, 18, 19, 17, 16, 16, 15, 13, 13, 12, 10, 9, 10, 8]}, "macron" : [17, 15, 14, 15, 13, 12, 10, 9, 9, 8, 8, 7, 8, 6], "ceremonie" : [1, 1, 2, 1, 3, 4, 5, 6, 6, 5, 4, 4, 3, 3], "aeroport" : [3, 3, 2, 3, 3, 4, 2, 2, 4, 3, 3, 3, 4, 4], "tempete" : [5, 5, 5, 4, 5, 4, 4, 5, 5, 6, 6, 5, 5, 4], "impot" : [20, 18, 19, 17, 16, 16, 15, 13, 13, 12, 10, 9, 10, 8]}

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


trend = res.trend
resplot = res.plot()
<<<<<<< HEAD
data_add
trend_by_period(data_add, 7)
=======

data_bis = {"trump" : [0, 1, 1, 3, 2, 4, 5, 5, 6, 8, 7, 9, 11, 10], "macron" : [17, 15, 14, 15, 13, 12, 10, 9, 9, 8, 8, 7, 8, 6], "ceremonie" : [0, 0, 2, 1, 3, 4, 5, 6, 6, 5, 4, 4, 3, 3], "aeroport" : [3, 3, 2, 3, 3, 4, 2, 2, 4, 3, 3, 3, 4, 4], "tempete" : [5, 5, 5, 4, 5, 4, 4, 5, 5, 6, 6, 5, 5, 4], "impot" : [20, 18, 19, 17, 16, 16, 15, 13, 13, 12, 10, 9, 10, 8]}
>>>>>>> 5800095a83a43fd2b2795db8fd3424f7cb2cc329
