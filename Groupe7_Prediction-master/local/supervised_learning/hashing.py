# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics


# Import data
df = pickle.load(open('../../../recoded_data_group7', 'rb'))

# Delete duplicates and unrecoded labels
df.drop_duplicates(['title'], keep='last', inplace=True)
df = df[df['theme_recoded'] != 'delete']

# Fix random seed for reproducibility
np.random.seed(10)

# Split our df for train/test with a stratify strategy
xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme_recoded'], test_size=0.2,
                                                stratify=df['theme_recoded'])

# Create the transform with hashing strategy
vectorizer = HashingVectorizer(n_features=1000)

# Encode document
xtrain = vectorizer.transform(xtrain['content']).toarray()
xtest = vectorizer.transform(xtest['content']).toarray()

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
ytrain = ytrain.map(dict_classes)
ytest = ytest.map(dict_classes)


def model_assessment(model, model_name):
    """
    Take a model and it's name in parameters, train a classifier and print the
    classification report, the confusion matrix, and the accuracy score.
    """
    labels = ['international', 'france', 'economie', 'sciences_high_tech',
              'arts_et_culture', 'sports', 'sante']
    clf = model.fit(xtrain, ytrain)
    predicted = clf.predict(xtest)
    print('--- %s results ---\n' % model_name)
    print(metrics.classification_report(ytest, predicted, target_names=labels))
    print('Confusion matrix:\n%s' % metrics.confusion_matrix(ytest, predicted))
    print('\nAccuracy score : %s' % metrics.accuracy_score(ytest, predicted))


model_assessment(SGDClassifier(loss='log', penalty='l2', alpha=1e-5, random_state=10,
                               max_iter=100, tol=None), 'Logistic Regression with SGD')
model_assessment(LinearSVC(C=1, random_state=10), 'Linear SVM')
