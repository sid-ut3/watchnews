"""
============================================================================
-*- coding: utf-8 -*-
Created on Wed Jan 10 13:57:06 2018

@author: Paul LAFAURIE, Clément BRANDAO, Tom COGNIN

============================================================================
"""

import pickle
from functions.g5_clean_text import clean_symbols
from functions.g5_tokenize import tokeniz
from functions.g5_handing_entity import handing_entity
# stop_words = pickle.load(open('./functions/stopwords.p', 'rb'))
stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/' +
                              'functions/stopwords.p', 'rb'))

"""
============================================================================
    links
============================================================================
"""

# LINK ON SERVER
path_source = '/var/www/html/projet2018/data/clean/robot'
path_target = '/var/www/html/projet2018/data/clean/filtering'

# TEST LINK
# path_source = '../Data/source_press_article'
# path_target = '../Data/target_press_article'

"""
============================================================================
    import json
============================================================================
"""


def analys_token(article, text_token, entity_, is_title=False):
    """
        Summary:
            This function creates the dictionnary.
            Requires global variable "stop_words"
        In:
            - text_token: list of tokenized word
            - entity_: list of named entities, whitespaces are underscores
            - is_title: boolean:
                    * 'True' if text_token contains the title,
                    * 'False' if it's the actual article content.
        Out:
            - info_token : a dictionnary:
                each compartiment is a dictionnary which contains informations
                for each words
            - post_w : info_token minus the stopwords
            - info_without : processed title without stopwords
    """
    info_token = {}
    i = 1
    for token in text_token:
        if str(token.text) in stop_words:
            tag = "STOPWORD"
        else:
            tag = token.pos_

        info_token[i] = {
            "word": token.text,
            "lemma": token.lemma_,
            "pos_tag": tag,
            "type_entity": entity_[str(token)]
            if str(token) in entity_.keys()
            else "",
            "position": i,
            "title": (
                set(str(token.text).upper().replace("_",
                    " ").split()).issubset(article["title"].upper(
                            ).split(" ")))
        }
        i += 1

    info_without = [token for token in info_token.values() if str(
        token["pos_tag"]) != "STOPWORD" and token["word"] != '.']

    if not is_title:
        post_w = {"article": {"date_publication": article["date_publi"],
                              "name_newspaper": article["newspaper"],
                              "surname_author": article["author"]
                              }, "position_word": info_without}
        info_token["words"] = [tkn.text for tkn in text_token]
        info_token["list_lemma"] = [tkn.lemma_ for tkn in text_token]
        return post_w, info_token
    else:
        return info_without


def tag_text(article, is_title=False):
    """
        Summary:
        In:
            - article: content of the article
            - f_stopwords: boolean used with parameter "with_stopwords"
            from analys_token
        Out:
            2 results (see analys_tokens)
            if is_title = True:
                - a dict with a list of all the words in the title processed
                and without stopwords
           if is_title = False:
               - a list of all the words striped of stopwords
               - a list of all the words
               both with stems and pos-tags and a flag if the word is
               named entity
    """
    if is_title:
        text = article["title"]
    else:
        text = article["content"]
    # remove punctuation
    clean_text = clean_symbols(text)
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)

    return analys_token(article, tokens, entity_, is_title=is_title)
