# -*- coding: utf-8 -*-
# group 7

import pandas as pd
import pickle
import glob


def import_data(recoded=False):
    frames = []
    for file_path in glob.glob('../../../../data/data_group5/*.json'):
        article = pd.read_json(file_path, typ='series')
        try:
            article = pd.Series({'title':article['title'], 'theme':article['theme'],
                                 'list_lemma':article['content']['list_lemma'],
                                 'source':article['newspaper']
                                 })
            article = article.to_frame().transpose()
            frames.append(article)
        except:
            # Do nothing
            pass
    df = pd.concat(frames)
    df.reset_index(drop=True, inplace=True)
    # Finally recode the categories if desired
    if recoded:
        # Load recoding dictionaries
        all_dicts = pickle.load(open('all_dicts', 'rb'))
        sources = ['Le Monde', 'Le Figaro', 'Liberation', 'Nouvel Obs', 'Telerama',
                   'Futura Sciences']
        df['theme_recoded'] = 'delete'
        # Recode each source in the list of sources
        for source,  source_dict in zip(sources, all_dicts):
            mask = df['source'] == source
            df.loc[mask, 'theme_recoded'] = df.loc[mask, 'theme'].map(source_dict)
        df['theme_recoded'] = df['theme_recoded'].fillna('delete')
    return df


df_recoded = import_data(recoded=True)

# Save our Dataframe in a pickle file
pickle.dump(df_recoded, open('../../../recoded_data_group5', 'wb'))