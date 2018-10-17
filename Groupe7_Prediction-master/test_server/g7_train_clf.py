# -*- coding: utf-8 -*-
# group 7

import lightgbm as lgb
import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from g7_import_data import import_data


# Import recoded data
df = import_data(recoded=True)

# Delete duplicates and unrecoded labels
df.drop_duplicates(['title'], keep='last', inplace=True)
df = df[df['theme_recoded'] != 'delete']

# Join lemmatized words
df['list_lemma'] = df['list_lemma'].map(lambda x: ' '.join(x))

# Fix random seed for reproducibility
np.random.seed(10)

# Create the transform with tfidf strategy
vectorizer = TfidfVectorizer(max_df=0.80, min_df=2, max_features=10000)

# Tokenize and build vocabulary
vectorizer.fit(df['list_lemma'])
vocabulary = vectorizer.vocabulary_

# Encode document
xtrain = vectorizer.transform(df['list_lemma']).toarray()

dict_classes = {
            'international': 0,
            'france': 1,
            'economie': 2,
            'sciences_high_tech': 3,
            'arts_et_culture': 4,
            'sports': 5,
            'sante': 6
            }

# Recode our output
ytrain = df['theme_recoded'].map(dict_classes)

# Train our classifier
lgb_train = lgb.Dataset(xtrain, ytrain)

best = {
        'bagging_fraction': 0.95,
        'feature_fraction': 1.0,
        'num_leaves': 20,
        'reg_alpha': 0.5,
        'metric': 'multi_error',
        'application': 'multiclass',
        'learning_rate': [0.1],
        'bagging_seed': 1,
        'feature_fraction_seed': 2,
        'num_class': 7
        }

clf = lgb.train(best, lgb_train, num_boost_round=450)

# Save it in a pickle file
pickle.dump(vectorizer, open('g7_vectorizer', 'wb'))
pickle.dump(clf, open('g7_clf', 'wb'))
