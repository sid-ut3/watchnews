#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:58:41 2018

@author: sid
"""
import pickle
data_non_supervised=pickle.load(open('data_non_supervised', 'rb'))

import numpy as np
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
kmeans.fit(data_non_supervised)
clusters = kmeans.labels_
clusters=clusters[:,None]
clusters=np.array(clusters,object)
data_clusters = np.concatenate((clusters,data_non_supervised), axis=1)
kmeans.cluster_centers_
idk = np.argsort(kmeans.labels_)
idk

#numpy groups

#Codage
#'rate_angry':11, 'rate_surprise':12,'rate_positivity':13,'rate_negativity':14,
#'rate_joy';15,'rate_fear'16,'rate_sadness':17,'rate_disgust':18,
#'rate_subjectivity':19, 'international':20,'france':21, 'economie':22,
# 'sciences_high_tech':23, 'arts_et_culture':24, 'sports':25, 'sante':26

#Division in cluster group
cluster1=data_clusters[np.where(data_clusters[:,0] == 0)] 
cluster2=data_clusters[np.where(data_clusters[:,0] == 1)] 
cluster3=data_clusters[np.where(data_clusters[:,0] == 2)] 
cluster4=data_clusters[np.where(data_clusters[:,0] == 3)] 
cluster5=data_clusters[np.where(data_clusters[:,0] == 4)] 
cluster6=data_clusters[np.where(data_clusters[:,0] == 5)] 


#Semantic and category mean for each cluster

np.mean(cluster1[:,11:27], axis=0) 
#Interpretation group1
#Dans ce groupe on retrouve les articles internationnaux (moyenne de 1 pour internationnal), ou l'on retrouve un peu plus
# de negativité de colére et de peur par rapport aux autres cluster (cluster1: Articles Internationaux Plutôt orienté négatif)
np.mean(cluster2[:,11:27], axis=0)
#Interpretation group2
#Ici l'on retrouve que des articles Français(moyenne de 1), ou le taux de surprise est le plus haut de tout les clusters 
# et un taux de positivté plutôt au dessus (Cluster2 : Articles Français orienté surprise,positif)
np.mean(cluster3[:,11:27], axis=0)
#Interpretation group3
#Ici l'on retrouve que des aricles arts et culture(moyenne de 1), dont le taux de subjectivité est beaucoup plus élevé que les autres groupes(0.28)
#Ceci est logique car la culture est subjectif d'une personne à une autres(Cluster3 : Art et culture subjectif)
np.mean(cluster4[:,11:27], axis=0)
#Interpretation group4
#Dans le group 4 on se départage entre sports et science high-tech respectivement (0.5 et 0.45), (cluster4 : Articles science et sport)
np.mean(cluster5[:,11:27], axis=0)
#Interpretation group5
#Dans ce groupe on retrouve les articles économiques(moyenne de 1 pour économique) orienté trés positif, le plus haut taux de tout les clusters
#(Cluster5: Articles économique positif)



#Interpretation

#Plot en cours de faire marcher

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()