# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence


# Import data
df = pickle.load(open('../../../recoded_filtered_data_group7', 'rb'))

# Delete duplicates and unrecoded labels
df.drop_duplicates(['title'], keep='last', inplace=True)
df = df[df['theme_recoded'] != 'delete']

# Fix random seed for reproducibility
np.random.seed(10)

# Split our df for train/test with a stratify strategy
xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme_recoded'], test_size=0.2,
                                                stratify=df['theme_recoded'])

# Implement a tokenizer
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(df['content'])

word_index = tokenizer.word_index

# Transform our texts in vectors of numbers
xtrain = tokenizer.texts_to_sequences(xtrain['content'])
xtrain = sequence.pad_sequences(xtrain, maxlen=500)
xtest = tokenizer.texts_to_sequences(xtest['content'])
xtest = sequence.pad_sequences(xtest, maxlen=500)

labels = ['international', 'france', 'economie', 'sciences_high_tech',
          'arts_et_culture', 'sports', 'sante']

def labels_to_vector(labels, y_output):
    output = []
    # Create an empty array for our output
    output_empty = [0] * len(labels)
    for i in y_output:
        # Output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[labels.index(i)] = 1
        output.append(output_row)
    y_output = output
    return y_output

# Transform our labels in vectors of booleans
ytrain = labels_to_vector(labels, ytrain)
ytest = labels_to_vector(labels, ytest)


# Save our training and testing base in a pickle file
train_test = [xtrain, xtest, ytrain, ytest]
pickle.dump(train_test, open('../../../train_test_deep_learning_group7', 'wb'))