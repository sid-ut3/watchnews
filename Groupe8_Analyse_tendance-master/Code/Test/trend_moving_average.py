"""

inter-promo project
group n°8

author: nicolas paillier

this program aims:
    - to extract words (keys) and values from a json file containing the
        whole of relevant terms and their sum of term frequencies per day
    - to calculate the moving average series for each word
    - to lead statistical tests in order to determine the trend (rise, drop)
        according to the t-test value

"""



"""

packages

"""

import numpy as np
import scipy.stats



"""

functions

"""

def extract_keys_values(data):
    """
    goal of this function :
        - to extract keys (ie. words) and values from the json file
    input parameter :
        - json file's content (data)
    output :
        - two lists (keys and values)
    """
    
    #initialisation
    keys = []
    values = []
    
    #for each entry in the json file
    for k, v in data.items():
        keys.append(k)
        values.append(v)
    
    return(keys, values)



def moving_average(seq, order) :
    """
    goal of this function :
        - to calculate the moving average
    input parameters :
        - list of values (seq)
        - interger (order)
    output :
        - list of values (moving_avg)
    """
    
    moving_avg = np.cumsum(seq, dtype = float)
    moving_avg[order:] = moving_avg[order:] - moving_avg[:-order]

    return moving_avg[order - 1:] / order



def test_trend(data, word, id_day):
    """
    goal of this function :
        - to calculate the t-test for the means of two independant samples
        - to return the trend (increasing or decreasing)
    input parameters :
        - data
        - word
        - id_day
    """
    
    test = scipy.stats.ttest_ind(data[word][id_day], data[word][id_day - 1])
    
    if (test[1] > 0.001 and test[1] < 0.05):
        if ((test[0] > 0)):
            return(word, "increasing_trend")
        elif (test[0] < 0):
            return(word, "decreasing_trend")
        else:
            return(word, "no_trend")
    elif (test[1] < 0.001):
        if ((test[0] > 0)):
            return(word, "strongly_increasing_trend")
        elif (test[0] < 0):
            return(word, "strongly_decreasing_trend")
        else:
            return(word, "no_trend")
    else:
        return(word, "no_trend")



def file_trend(data):
    """
    goal of this function :
        - data preprocessing for group n°9 (web)
    input parameter :
        - data (json file)
    output :
        - dict containing the trend for each word
    """
    
    output_trend = {}

    for key, value in data.items():
        if(key != 'period'):
            for val in range(1, len(value)):
                word, trend = test_trend(data, key, val)
            output_trend[key] = trend
        else:
            output_trend[key] = value

    return(output_trend)



def trend_with_moving_average(data_v2):
    """
    goal of this function :
        - to calculate the moving average for each word
            (ie. each entry in the json file)
        - to determine the trend (increasing or decreasing)
    input parameters :
        - data (json format)
    intermediary actions :
        - extraction of keys and values (function)
    output :
        - dict with many words and their trend (cf. file_trend function)
    """
    
    keys, values = extract_keys_values(data_v2)
    
    mavg_series = []
    dict_word_mavg = {}

    #for each word in the json file (ie. data_v2)
    for j in range(len(values)):
        mavg_series = moving_average(values[j], 3).tolist()
        splt_series = [mavg_series[0:5], mavg_series[6:11]]
        dict_word_mavg[keys[j]] = splt_series
    
    return(file_trend(dict_word_mavg))