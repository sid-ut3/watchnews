# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:54:19 2018

@author: laura
"""
#g3
#MI_AH_CG_LB


#Déclarations
words = [] 
article = []
number_words = REQUETE1
number_article= REQUETE1_BIS
day = {}
week = {}
month = {}
i=0
list_tf_idf_day = []
list_tf_idf_previous_day = []

#Donne le nombre de mot dans les articles du jour
while number_words > 0 : 
    words [number_words] = REQUETE2 (number_words)
    number_words = number_words-1

#Donne le nombre d'article publiés ce jour
while number_article > 0 : 
    article [number_article] = REQUETE2BIS (number_article)
    number_article = number_article-1


# renvoie le tf et l'idf de chaque article pour chaque mot le jour j-1 et le jour j 
for i in range len (words) : 
    for k in range len (article) :
        list_tf_idf_day.append (REQUETE3 (words[i], article[j], 0))
        list_tf_idf_previous_day.append (REQUETE3 ( words[i], article[j] ,1))
    day [ words[i] ] = [ list_tf_idf_previous_day, list_tf_idf_day ]
    
    
#renvoie le tf et l'idf de chaque article pour chaque mot pour chaque jour de la semaine
for i in range len (words) :
    for j in range (7) :
        while number_article > 0 : 
            article [number_article] = REQUETE2BIS (number_article)
            number_article = number_article-1
        for k in range len(article) : 
            list_tf_idf.append (REQUETE3 (words [i] , article [k] , 6-j ))
            list_tf.append (REQUETE3_BIS (words [i] , article [k] , 6-j))
    week [ words[i] '_tf_idf' ] = list_tf_idf []
    week [ words[i] '_tf' ] = list_tf
    
    
#renvoie le tf et l'idf de chaque article pour chaque mot pour chaque jour du mois
for i in range len (words) :
    for j in range (30) :
         while number_article > 0 : 
            article [number_article] = REQUETE2BIS (number_article)
            number_article = number_article-1
        for k in range len(article) : 
            list_tf_idf.append (REQUETE3 (words [i] , article [k] , 29-j ))
            list_tf.append (REQUETE3_BIS (words [i] , article [k] , 29-j))
    week [ words[i]'_tf_idf' ] = list_tf_idf []
    week [ words[i]'_tf' ] = list_tf
    
    
#les tf idf entre quotes ne passent pas à la compilation


