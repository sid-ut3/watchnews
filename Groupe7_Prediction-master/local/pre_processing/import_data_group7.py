# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob


def import_data(recoded=False):
    frames = []
    df = pd.DataFrame()
    # Load recoding dictionnaries
    all_dicts = pickle.load(open('all_dicts', 'rb'))
    sources = ['lemonde', 'lefigaro', 'liberation', 'nouvelobs', 'telerama',
               'futurasciences']
    for source,  source_dict in zip(sources, all_dicts):
        frames = []
        for file_path in glob.glob('../../../../data/data_group7/%s/*.json' % source):
            article = pd.read_json(file_path, typ='series')
            article = pd.Series({'title':article['title'], 'theme':article['theme'],
                                 'content':article['content'], 'source':article['newspaper']
                                 })
            article = article.to_frame().transpose()
            frames.append(article)
        # Concatenante all articles from the site in a single Dataframe
        frames = pd.concat(frames)
        # Recode categories from the source if desired
        if recoded:
            frames['theme_recoded'] = frames['theme'].map(source_dict)
        # Concatenate with other sources in a single Dataframe
        df = pd.concat([df, frames])
    df.reset_index(drop=True, inplace=True)
    return df


df_recoded = import_data(recoded=True)

# Save our Dataframes in a pickle file
pickle.dump(df_recoded, open('../../../recoded_data_group7', 'wb'))