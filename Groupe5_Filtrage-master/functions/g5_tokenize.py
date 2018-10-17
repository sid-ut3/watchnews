"""
============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Clément BRANDAO

Function : Get Part-of-Speech Tags for every word
============================================================================
"""
import spacy
nlp = spacy.load('fr')


def tokeniz(text):  # Tokenize a text with library Spacy
    """
        Summary: Transorm all the text  where each word become tokens
        tokens
        In:
            - article: content of the article
        Out:
            - tokenize article, each word is a token which we can apply some
            functions as .text, . lemma etc ...
    """
    simple_art = text.replace("'", " ")
    doc = nlp(simple_art)
    return doc
