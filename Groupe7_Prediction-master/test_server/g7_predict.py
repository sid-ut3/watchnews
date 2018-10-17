# -*- coding: utf-8 -*-
# group 7

import pickle
import json

from g7_import_data import import_data


# Import our vectorizer and our classifier
vectorizer = pickle.load(open('g7_vectorizer', 'rb'))
clf = pickle.load(open('g7_clf', 'rb'))

# Import recoded data
df = import_data(recoded=True, to_predict=True)

# Join lemmatized words
df['list_lemma'] = df['list_lemma'].map(lambda x: ' '.join(x))

# Prepare our inputs
x_multi = vectorizer.transform(df['list_lemma']).toarray()

# Predict new labels
predicted_probas = clf.predict(x_multi)

dict_labels = {
        0: 'international',
        1: 'france',
        2: 'economie',
        3: 'sciences_high_tech',
        4: 'arts_et_culture',
        5: 'sports',
        6: 'sante'
        }

# Get multi-labels list and list boolean for strongest label
multi_labels = [
        [[dict_labels[i] for i, p in enumerate(probas) if p > 0.1],
          [int(i == probas.argmax()) for i, p in enumerate(probas) if p > 0.1]]
        for probas in predicted_probas
        ]

# Create our list of dictionaries with the good format for the database
post_db = [
        {"id_article": i, "label": j[0], "strongest_label": j[1]}
        for (i, j) in zip(df['id'], multi_labels)
        ]

# Save it in a json file for the database
with open('g7_themes_multi_labels.json', 'w') as f:
    json.dump(post_db, f)
