# -*- coding: utf-8 -*-
# group 7

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans


# Import data
data = pickle.load(open('data_non_supervised', 'rb'))

# Let's fit our clustering
kmeans = KMeans(n_clusters=5, random_state=10)
kmeans.fit(data)

# Get clusters for each observations
clusters = kmeans.labels_
clusters = clusters[:, None]

# Get cluster centers value for each initial variable
cols = ['rate_angry', 'rate_surprise', 'rate_positivity', 'rate_joy',
        'rate_negativity', 'rate_fear', 'rate_sadness', 'rate_disgust',
        'rate_subjectivity', 'international', 'france', 'economie',
        'sciences_high_tech', 'arts_et_culture', 'sports', 'sante']
cluster_centers = kmeans.cluster_centers_
cluster_centers = pd.DataFrame(cluster_centers[:, 10:], columns=cols)

# Save our k-means
pickle.dump(kmeans, open('g7_k_means', 'wb'))

## CAH
#cah = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
#cah.fit(data)
#cah_clusters = cah.labels_

distortions = []
K = range(1,30)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(data)
    kmeanModel.fit(data)
    distortions.append(sum(np.min(cdist(data, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / data.shape[0])

# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title(' La méthode Elbow Show pour identifier le nombre de groupe k optimal')
plt.show()
