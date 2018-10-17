# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:15:24 2018

@author: Nicolas
"""

import json
import numpy

# Reading JSON data
with open('score_weekV2.json', 'r') as file:
    file = json.load(file)


def score_week(file, top_word):
    '''
Function calculate mean TF IDF by word to built a dictionnary of word most
important
Function has two parameters:
    file : Json File
    top_word : number of important word which user would
It returns a dictionnary of top word with their mean TF IDF
A second dictionnary with top word with their TF values
'''''

    agregate = 0
    counter = 0
    key_word = {}
    dico_back = {}
    list_mean_intermediate = []
    dico_mean = {}

    for key, val in file.items():
        if key != "Period" and key[-4:] != "type":
            dico_mean[key] = val[7:14]

    # calculate mean TF IDF by word
    for key, val in dico_mean.items():
        for index1 in range(len(val)):
            if key != "Period" and key[-4:] != "type":
                for index2 in range(len(val[index1])):
                    agregate = agregate + float(val[index1][index2])
                    counter = counter + 1
                if counter == 0:
                    list_mean_intermediate.append(0)
                else:
                    list_mean_intermediate.append(agregate/counter)

                key_word[key] = numpy.mean(list_mean_intermediate)
                agregate = 0
                counter = 0

    # sort words in descending order
    key_word_sort = sorted(key_word.items(), reverse=True, key=lambda t: t[1])

    # get only the number of key word pick by user
    key_word = key_word_sort[0:top_word]

    # get TF IDF of key word

    for k, v in key_word:
        dico_back[k] = v

    dictionnary_intermediate = {}
    for key_dico_back in dico_back.keys():
        dictionnary_intermediate[key_dico_back] = file.get(key_dico_back)

    dico_tf = {}
    liste_agregate = []

    for key, val in dictionnary_intermediate.items():
        for index1 in range(len(val)):
            if len(val[index1]) != 0:
                for index2 in range(len(val[index1])):
                    agregate = agregate + float(val[index1][index2])
            else:
                agregate = 0
            liste_agregate.append(agregate)
            agregate = 0
        dico_tf[key] = liste_agregate
        liste_agregate = []

    return(dico_back, dico_tf)


print(score_week(file, 10))
