"""
============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 11 2018

@author: Maxime BRIENS

============================================================================
"""
import requests

SERVER_URL = 'http://localhost:5005'


def post_filtering(json):
        """
        Summary:
            This functions is posting informations
            about articles and filtering in the database.
        In:
            - text: article in the correct shape for posting
        Out:
            - art: log of posts.
    """
    url_POS = SERVER_URL + '/filtering'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, data=json)
    return response


def post_tfidf(json):
    """
        Summary:
            This functions is posting informations
            about tf-idf of lemmas of each articles.
        In:
            - text: tf-idf in the correct shape for posting
        Out:
            - art: log of posts.
    """
    url_POS = SERVER_URL + '/tfidf'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, data=json)
    return response
