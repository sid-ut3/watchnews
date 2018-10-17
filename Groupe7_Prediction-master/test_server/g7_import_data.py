# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob
import os


def import_data(recoded=False, to_predict=False):
    """
    Take in parameter if we want to recode the themes and if we want to import
    all articles or just the ones for which we have not send themes predicted
    to the DB. Then return data we need (id, source, theme, title, list_lemma,
    theme_recoded) in a pandas dataframe.
    """
    frames = []
    path = '/var/www/html/projet2018/data/clean/semantic/all_articles'
    if to_predict:
        path = '/var/www/html/projet2018/data/clean/semantic/to_predict'
    for file_path in glob.glob('%s/*.json' % path):
        article = pd.read_json(file_path, typ='series')
        # Sometimes there are errors when parsing some articles (we found articles
        # that doesn't have a list_lemma key for example)), so we need to
        # prevent it with a try/except block
        try:
            article = pd.Series({'id': article['article']['id_art'],
                                 'source': article['article']['name_newspaper'],
                                 'theme': article['article']['theme'],
                                 'title': article['article']['title'],
                                 'list_lemma': article['list_lemma'],
                                 'rate_angry': article['article']['rate_angry'],
                                 'rate_disgust': article['article']['rate_disgust'],
                                 'rate_fear': article['article']['rate_fear'],
                                 'rate_joy': article['article']['rate_joy'],
                                 'rate_negativity': article['article']['rate_negativity'],
                                 'rate_positivity': article['article']['rate_positivity'],
                                 'rate_sadness': article['article']['rate_sadness'],
                                 'rate_subjectivity': article['article']['rate_subjectivity'],
                                 'rate_surprise': article['article']['rate_surprise']
                                 })
            article = article.to_frame().transpose()
            frames.append(article)
            if to_predict:
                # Delete the article in the repository
                os.remove(file_path)
        except:
            # Do nothing
            pass
    df = pd.concat(frames)
    df.reset_index(drop=True, inplace=True)
    # Finally recode the categories if desired
    if recoded:
        # Load recoding dictionaries
        all_dicts = pickle.load(open('g7_all_dicts', 'rb'))
        sources = ['Le Monde', 'Le Figaro', 'Liberation', 'Nouvel Obs',
                   'Telerama', 'Futura Sciences']
        df['theme_recoded'] = 'delete'
        # Recode each source in the list of sources
        for source,  source_dict in zip(sources, all_dicts):
            mask = df['source'] == source
            df.loc[mask, 'theme_recoded'] = df.loc[mask, 'theme'].map(source_dict)
        df['theme_recoded'] = df['theme_recoded'].fillna('delete')
    return df
