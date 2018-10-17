# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# Import data
df = pickle.load(open('../../../recoded_data_group5', 'rb'))

# Delete duplicates and unrecoded labels
df.drop_duplicates(['title'], keep='last', inplace=True)
df = df[df['theme_recoded'] != 'delete']

# Join lemmatized words
df['list_lemma'] = df['list_lemma'].map(lambda x: ' '.join(x))

# Fix random seed for reproducibility
np.random.seed(10)

# Split our df for train/test with a stratify strategy
xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme_recoded'], test_size=0.2,
                                                stratify=df['theme_recoded'])

# Create the transform with tfidf strategy
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000)
# Tokenize and build vocabulary
vectorizer.fit(xtrain['list_lemma'])
vocabulary = vectorizer.vocabulary_
# Encode document
xtrain = vectorizer.transform(xtrain['list_lemma']).toarray()
xtest = vectorizer.transform(xtest['list_lemma']).toarray()

dict_classes = {
            'international':0,
            'france':1,
            'economie':2,
            'sciences_high_tech':3,
            'arts_et_culture':4,
            'sports':5,
            'sante':6
            }

# Recode our output
ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)

# Save our training and testing base in a pickle file
train_test = [xtrain, xtest, ytrain, ytest]
pickle.dump(train_test, open('../../../train_test_data_group5', 'wb'))