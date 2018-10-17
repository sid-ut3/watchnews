# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:18:49 2018
@author: Nicolas
"""

import json
import numpy

# Reading JSON data
with open('jour.json', 'r') as file:
    file = json.load(file)


def score_day(file, top_word):
    """
    the function's objectives :
        This function allows you to show the most important words of a
        newspaper
        article and the TF of the previous day and the day for each word.
        We place the number of words what we want in parameters of the function
        when we call it.
    the function's parameters :
        The two function's parameters are
        - the file json which contains datas
        - the number of words what we want
    the function returns
        - a dictionnary which contains the key words and their mean on two days
        - a dictionnary wich contains the key words and all corresponding
        values
    """
    agregate = 0
    counter = 0
    key_word = {}
    dico_tf = {}
    list_mean_intermediate = []
    # calculate mean TF IDF by word
    for key, val in file.items():
        if key != "period":
            for index1 in range(len(val)):
                for index2 in range(len(val[index1])):
                    agregate = agregate + float(val[index1][index2])
                    counter = counter + 1
                if counter != 0:
                    list_mean_intermediate.append(agregate / counter)
                else:
                    list_mean_intermediate.append(0)
            key_word[key] = numpy.mean(list_mean_intermediate)

            agregate = 0
            counter = 0

    # sort words in descending order
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word
    dico_back = {}
    for k, v in key_word:
        dico_back[k] = v

    # construct the value dictionary for each word
    list_agregate = []
    dico = {}
    for key_dico_back in dico_back.keys():
        dico_tf[key_dico_back] = file.get(key_dico_back)
    for key, val in dico_tf.items():
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    list_agregate.append(float(val[index1][index2]))
            else:
                list_agregate.append(0)
        dico[key] = list_agregate
        list_agregate = []

    return(dico_back, dico)


print(score_day(file, 10))
